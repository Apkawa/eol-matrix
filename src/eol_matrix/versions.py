import datetime
from typing import TypedDict

from eol_matrix.runtimes import get_runtime
import requests
from packaging.specifiers import SpecifierSet
from packaging.version import Version

from eol_matrix.endoflife_client import EndOfLifeClient
from eol_matrix.runtimes.python import PythonVersion
from eol_matrix.types import LibraryData, ReleaseData


class RuntimePackageVersions:
    runtime_name: str
    package_name: str
    _versions: list[LibraryData] | None = None
    _runtime_releases: list[ReleaseData] | None = None
    _package_releases: list[ReleaseData] | None = None

    def __init__(
        self,
        runtime_name: str,
        package_name: str,
        versions: list[LibraryData] | None = None,
    ):
        self.runtime_name = runtime_name
        self.package_name = package_name
        self._versions = versions

    def _get_versions(self) -> list[LibraryData]:
        if self._versions is not None:
            return self._versions
        runtime_version_cls = get_runtime(self.runtime_name)
        rt = runtime_version_cls()
        self._versions = rt.get_package_versions(self.package_name)
        return self._versions

    def get_runtime_releases(self) -> list[ReleaseData]:
        if self._runtime_releases:
            return self._runtime_releases
        c = EndOfLifeClient()
        # TODO глобальный кеш
        versions = c.get_all_versions(self.runtime_name)
        releases: list[ReleaseData] = []
        for v in versions:
            releases.append(
                {
                    "date": datetime.datetime.fromisoformat(v["releaseDate"]).date(),
                    "version": Version(v["name"]),
                    "isEol": v["isEol"],
                }
            )
        self._runtime_releases = releases
        return releases

    def get_package_eol_releases(self) -> list[ReleaseData]:
        if self._package_releases is not None:
            return self._package_releases
        c = EndOfLifeClient()
        try:
            versions = c.get_all_versions(self.package_name)
        except requests.HTTPError as e:
            if e.response.status_code == 404:
                self._package_releases = []
                return self._package_releases
            raise e
        releases: list[ReleaseData] = []
        for v in versions:
            releases.append(
                {
                    "date": datetime.datetime.fromisoformat(v["releaseDate"]).date(),
                    "version": Version(v["name"]),
                    "isEol": v["isEol"],
                }
            )
        self._package_releases = releases
        return releases

    def get_runtime_version_by_release(self, dt: datetime.date) -> ReleaseData:
        """
        Получаем максимальную версию рантайма на момент даты
        """
        runtimes_filtered = [r for r in self.get_runtime_releases() if r["date"] <= dt]
        return list(reversed(sorted(runtimes_filtered, key=lambda r: r["version"])))[0]

    def remove_eol_versions(self, versions: list[LibraryData]) -> list[LibraryData]:
        live_releases = [p for p in self.get_package_eol_releases() if not p["isEol"]]
        if not live_releases:
            return versions
        spec = [SpecifierSet(f"~={p['version']}.0") for p in live_releases]

        def spec_check(v: Version) -> bool:
            return not not [s for s in spec if s.contains(v)]

        return [v for v in versions if spec_check(v["version"])]

    def get_versions(self, runtime_version: Version | str | None = None) -> list[LibraryData]:
        """
        Наивная проверка версий которая не учитывает ломающие релизы которые вышли позже
        """
        versions: list[LibraryData] = []
        if type(runtime_version) is str:
            runtime_version = Version(runtime_version)

        for v in self._get_versions():
            version_runtime = v["runtime_version"]
            if (
                runtime_version
                and version_runtime
                and not version_runtime.contains(runtime_version)
            ):
                continue
            versions.append(v)
        return sorted(versions, key=lambda v: v["version"])

    def get_versions_by_releases(
        self, runtime_version: Version | str | None = None
    ) -> list[LibraryData]:
        """
        Проверяем по релизам сверху
        """
        versions: list[LibraryData] = []
        if type(runtime_version) is str:
            runtime_version = Version(runtime_version)

        for v in self._get_versions():
            version_runtime = v["runtime_version"]
            # todo мб надо брать следующую версию и делать <
            released_runtime = self.get_runtime_version_by_release(v["date"])
            released_runtime_specifer = SpecifierSet(f"<={released_runtime['version']}")
            if version_runtime:
                version_runtime = version_runtime & released_runtime_specifer
            else:
                version_runtime = released_runtime_specifer
            if version_runtime.is_unsatisfiable():
                continue
            if runtime_version and not version_runtime.contains(runtime_version):
                continue
            versions.append(v)
        return sorted(versions, key=lambda v: v["version"])
