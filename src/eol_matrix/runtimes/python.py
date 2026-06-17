from datetime import datetime

import requests
from packaging.specifiers import SpecifierSet
from packaging.version import Version

from eol_matrix.runtimes.base import BaseRuntimeVersion
from eol_matrix.types import LibraryData


class PythonVersion(BaseRuntimeVersion):
    name = "python"

    def get_runtime_version(self, package: str, version: str) -> SpecifierSet | None:
        """
        Шаг 2: Запрашиваем из PyPI ограничение на версию Python для конкретного пакета.
        Возвращает строку вида '>=3.10'
        """
        url = f"https://pypi.org/pypi/{package}/{version}/json"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        version_set = data["info"]["requires_python"] or None
        return version_set and SpecifierSet(version_set)

    def get_package_versions(self, package: str) -> list[LibraryData]:
        """ """
        url = f"https://pypi.org/pypi/{package}/json"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        releases = data["releases"]
        versions: list[LibraryData] = []
        for v, r in releases.items():
            if not r:
                continue
            runtime_version = r[0]["requires_python"] or None
            ver: LibraryData = {
                "version": Version(v),
                "date": datetime.fromisoformat(r[0]["upload_time"]).date(),
                "runtime_version": runtime_version and SpecifierSet(runtime_version),
            }
            versions.append(ver)
        return versions
