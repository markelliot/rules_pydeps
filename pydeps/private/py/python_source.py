import pathlib
from typing import Any, override

from pydeps.private.py import python_module as pm


class SourceFile:
    def __init__(self, relative_path: pathlib.Path) -> None:
        if relative_path.is_absolute():
            raise ValueError(
                f"SourceFile must be a relative path, found {relative_path}."
            )
        self._path = relative_path

    def module(self) -> pm.PythonModule:
        return pm.PythonModule.from_path(self._path)

    def path(self) -> pathlib.Path:
        return self._path

    @override
    def __eq__(self, other: Any) -> bool:
        return isinstance(other, SourceFile) and self._path == other._path

    @override
    def __hash__(self) -> int:
        return hash(self._path)

    @override
    def __repr__(self) -> str:
        return f"SourceFile({self._path})"

    @override
    def __str__(self) -> str:
        return str(self._path)
