"""
Базовый класс райнтайма, включает в себя интерфейса поиска по апи
Например для питона - pypi, для node - npm и тд
"""

from abc import ABC, abstractmethod

import requests
from packaging.specifiers import SpecifierSet

from eol_matrix.types import LibraryData


class BaseRuntimeVersion(ABC):
    name: str

    @abstractmethod
    def get_runtime_version(self, package: str, version: str) -> SpecifierSet | None: ...

    @abstractmethod
    def get_package_versions(self, package: str) -> list[LibraryData]:
        """
        Список версий cгруппированый по runtime_version
        """
        ...
