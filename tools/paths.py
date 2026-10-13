"""Portable relative paths shared by the offline validators."""

from pathlib import Path, PurePosixPath
import re


def safe_relative(value: object) -> bool:
    if not isinstance(value, str) or not value or value == ".":
        return False
    if any(character in value for character in '\\:<>"|?*'):
        return False
    if any(ord(character) < 32 for character in value):
        return False
    path = PurePosixPath(value)
    return (
        not path.is_absolute()
        and value == path.as_posix()
        and ".." not in path.parts
        and all(
            not part.endswith((".", " "))
            and not re.fullmatch(
                r"(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])", part.split(".")[0], re.I
            )
            for part in path.parts
        )
    )


def contained_file(root: Path, relative: object) -> bool:
    return safe_relative(relative) and (root / relative).resolve().is_relative_to(
        root.resolve()
    )
