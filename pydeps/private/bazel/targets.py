"Datatypes and protocols for Bazel targets."

import pathlib
from typing import Self


class BazelTarget(str):
    """A typed wrapper around an absolute Bazel target string of the form //path/to:target."""

    @classmethod
    def from_target(cls, package: pathlib.Path, target: str) -> Self:
        return cls(cls._canonicalize(str(package), target))

    @classmethod
    def from_absolute(cls, target: str) -> Self:
        if not target.startswith("//"):
            raise ValueError(f"Target {target} is not an absolute Bazel path")
        return cls(cls._canonicalize_absolute(target))

    @classmethod
    def _canonicalize(cls, package: str, target: str) -> str:
        if target.startswith("//"):
            return cls._canonicalize_absolute(target)
        elif target.startswith(":"):
            # local reference explicitly
            return f"//{package}{target}"
        else:
            # the case where it's just a raw name
            return f"//{package}:{target}"

    @staticmethod
    def _canonicalize_absolute(target: str) -> str:
        if ":" not in target:
            last = target.split("/")[-1]
            return f"{target}:{last}"
        else:
            return target

    @property
    def target_name(self) -> str:
        return self.split(":", 2)[-1]

    @property
    def package(self) -> pathlib.Path:
        return pathlib.Path(self.removeprefix("//").split(":")[0])

    def relativize(self, relative_package: pathlib.Path) -> str:
        """
        Normalizes labels of the form //foo/bar/baz:baz to be relative to the supplied package:
        - When accessing `//foo/bar/baz:baz` from `foo/bar/baz`, render ":baz"
        - When accessing `//foo/bar/baz:baz` from anywhere else, render "//foo/bar/baz"
        - Else, render the current full label
        """
        # relative
        if relative_package == self.package:
            return f":{self.target_name}"

        # not relative, check to see if this is the implied target
        if self.package.name == self.target_name:
            return self.split(":", 2)[0]

        # it's not, just return the absolute target
        return self
