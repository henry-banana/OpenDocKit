"""Stable, readable diagnostics shared by maintainer checks."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Issue:
    code: str
    path: str
    message: str
