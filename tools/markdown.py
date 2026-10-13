"""Check local inline Markdown links without interpreting example code as links.

This is a deliberately limited Markdown check, not a CommonMark renderer.
External links and reference-style links are not fetched or validated.
"""

from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

from tools.issues import Issue


def readable_markdown(text: str) -> str:
    visible = []
    fence = None
    for line in text.splitlines():
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if (
                match
                and match[1][0] == fence[0]
                and len(match[1]) >= len(fence)
                and not match[2].strip()
            ):
                fence = None
            continue
        if match:
            fence = match[1]
            continue
        visible.append(line)
    text = re.sub(r"<!--.*?-->", "", "\n".join(visible), flags=re.S)
    return re.sub(r"`[^`\n]+`", "", text)


def heading_ids(text: str) -> set[str]:
    result = set()
    seen = {}
    for title in re.findall(r"^#{1,6}\s+(.+?)\s*$", readable_markdown(text), re.M):
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        result.add(slug if not count else f"{slug}-{count}")
    return result


def validate_links(
    root: Path, paths: list[Path], copy_roots: list[Path]
) -> list[Issue]:
    root = root.resolve()
    issues = []
    for path in paths:
        relative = path.relative_to(root).as_posix()
        if not path.resolve().is_relative_to(root):
            issues.append(Issue("UNSAFE_LINK", relative, "Resolved outside library."))
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            issues.append(Issue("MARKDOWN_PARSE", relative, str(error)))
            continue
        owning = next(
            (folder for folder in copy_roots if path.is_relative_to(folder)), None
        )
        for target in re.findall(
            r"(?<!!)\[[^\]\n]+\]\(([^)]+)\)", readable_markdown(text)
        ):
            target = target.strip().strip("<>")
            try:
                parsed = urlsplit(target)
            except ValueError as error:
                issues.append(Issue("UNSAFE_LINK", relative, str(error)))
                continue
            if parsed.scheme in {"http", "https", "mailto"}:
                continue
            if parsed.scheme or parsed.netloc:
                issues.append(Issue("UNSAFE_LINK", relative, target))
                continue
            destination = (
                (path.parent / unquote(parsed.path)).resolve()
                if parsed.path
                else path.resolve()
            )
            if not destination.is_relative_to(root):
                issues.append(Issue("UNSAFE_LINK", relative, target))
                continue
            if owning and not destination.is_relative_to(owning.resolve()):
                issues.append(
                    Issue(
                        "SHELF_LINK",
                        relative,
                        "Copy root depends on outside content: " + target,
                    )
                )
            if not destination.exists():
                issues.append(Issue("BROKEN_LINK", relative, target))
                continue
            if (
                parsed.fragment
                and destination.is_file()
                and destination.suffix in {".md", ".mdc"}
            ):
                try:
                    anchors = heading_ids(destination.read_text(encoding="utf-8"))
                except (OSError, UnicodeError) as error:
                    issues.append(
                        Issue("MARKDOWN_PARSE", relative, f"{target}: {error}")
                    )
                    continue
                if unquote(parsed.fragment) not in anchors:
                    issues.append(Issue("BROKEN_ANCHOR", relative, target))
    return issues
