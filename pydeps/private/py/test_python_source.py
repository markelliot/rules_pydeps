import pathlib

import pytest

from pydeps.private.py import python_module as pm
from pydeps.private.py import python_source as pys


def test__init__raise_absolute() -> None:
    with pytest.raises(ValueError):
        pys.SourceFile(pathlib.Path("/foo/bar/baz.py"))


def test__init__pass() -> None:
    path = pathlib.Path("foo/bar/baz.py")
    source = pys.SourceFile(path)
    assert source.module() == pm.PythonModule.from_path(path)


def test__path__roundtrip() -> None:
    path = pathlib.Path("foo/bar/baz.py")
    assert pys.SourceFile(path).path() == path
