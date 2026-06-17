from datetime import date

from packaging.specifiers import SpecifierSet
from packaging.version import Version

from eol_matrix.versions import LibraryData, RuntimePackageVersions


def test_get_versions():
    versions: list[LibraryData] = [
        {
            "version": Version("0.1"),
            "runtime_version": SpecifierSet(">=3.7"),
            # 3.10 release
            "date": date(2021, 1, 1),
        },
        {
            "version": Version("0.2"),
            "runtime_version": SpecifierSet(">=3.9"),
            # 3.11 release
            "date": date(2022, 1, 1),
        },
        {
            "version": Version("0.4"),
            "runtime_version": SpecifierSet(">=3.10"),
            # 3.12 release
            "date": date(2024, 1, 1),
        },
        {
            "version": Version("0.6"),
            "runtime_version": SpecifierSet(">=3.14"),
            "date": date(2026, 1, 1),
        },
    ]

    rp = RuntimePackageVersions("python", package_name="foo", versions=versions)
    assert rp.get_versions() == [
        Version("0.1"),
        Version("0.2"),
        Version("0.4"),
        Version("0.6"),
    ]
    # время после релиза 3.12
    assert rp.get_runtime_version_by_release(date(2024, 1, 1)) == {
        "date": date(2023, 10, 2),
        "version": Version("3.12"),
        "isEol": False,
    }
    # Наивная проверка
    assert rp.get_versions("3.12") == [
        Version('0.1'),
        Version('0.2'),
        Version("0.4"),
    ]

    assert rp.get_versions_by_releases("3.12") == [
        Version("0.4"),
    ]


def test_get_released_runtime():
    rp = RuntimePackageVersions("python", package_name="foo", versions=[])
    # время после релиза 3.12
    # 3.14 - 07 Oct 2025
    # 3.13 - 07 Oct 2024
    assert rp.get_runtime_version_by_release(date(2025, 9, 4)) == {
        "date": date(2024, 10, 7),
        "version": Version("3.13"),
        "isEol": False,
    }

    assert rp.get_runtime_version_by_release(date(2026, 9, 4)) == {
        "date": date(2025, 10, 7),
        "version": Version("3.14"),
        "isEol": False,
    }
