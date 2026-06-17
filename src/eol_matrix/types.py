
import datetime
from typing import TypedDict

from packaging.specifiers import SpecifierSet
from packaging.version import Version


class ReleaseData(TypedDict):
    version: Version
    date: datetime.date
    isEol: bool


class LibraryData(TypedDict):
    version: Version
    date: datetime.date
    runtime_version: SpecifierSet | None
