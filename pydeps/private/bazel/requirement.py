import dataclasses
from enum import Enum
from typing import Self


class Kind(str, Enum):
    PIP = "pip"


@dataclasses.dataclass(frozen=True, kw_only=True)
class Requirement:
    requirement: str
    kind: Kind

    @classmethod
    def from_raw(cls, raw: str, kind: Kind) -> Self:
        return cls(requirement=raw.replace("_", "-").lower(), kind=kind)

    def render(self) -> str:
        match self.kind:
            case Kind.PIP:
                return f'requirement("{self.requirement}")'

        raise ValueError("never")
