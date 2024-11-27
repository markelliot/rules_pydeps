"Tools for interacting with Bazel's external dependency directories."

import functools
import json
import pathlib

from pydeps.private.bazel import requirement as br
from pydeps.private.py import python_module as pm


def module_index(index: str) -> dict[pm.PythonModule, br.Requirement]:
    "Returns an index of module ownership to external requirement."
    return _module_index(
        _load_pip_deps_index(index)["module_to_requirement"], br.Kind.PIP
    )


def label_index(index: str) -> dict[str, br.Requirement]:
    "Returns an index of Bazel label to external requirement."
    return _label_index(_load_pip_deps_index(index)["label_to_requirement"])


@functools.cache
def _load_pip_deps_index(index: str) -> dict[str, dict[str, str]]:
    path = pathlib.Path(index)
    assert path.exists(), f"Unable to load pip_deps_index from {path}"
    with open(path, "r") as f:
        return json.load(f)


def _module_index(
    external_deps_manifest: dict[str, str], kind: br.Kind
) -> dict[pm.PythonModule, br.Requirement]:
    return {
        pm.PythonModule(module): br.Requirement.from_raw(raw=dep, kind=kind)
        for module, dep in external_deps_manifest.items()
    }


def _label_index(label_to_requirement: dict[str, str]) -> dict[str, br.Requirement]:
    return {
        label: br.Requirement.from_raw(raw=dep, kind=br.Kind.PIP)
        for label, dep in label_to_requirement.items()
    }
