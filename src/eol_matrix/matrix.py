
from packaging.version import Version
from typing_extensions import TypedDict

from eol_matrix.endoflife_client import EndOfLifeClient
from eol_matrix.types import LibraryData
from eol_matrix.versions import RuntimePackageVersions


class RuntimeMatrixData(TypedDict):
    packages: dict[str, list[LibraryData]]


class MatrixResultData(TypedDict):
    runtimes: dict[str, RuntimeMatrixData]


def deduplicate_versions(versions: list[LibraryData]) -> list[LibraryData]:
    """
    сжимает список версий до major.minor, заодно имеем время последнего релиза
    """
    m: dict[str, list[LibraryData]] = {}

    for vd in versions:
        v = vd["version"]
        m_v_key = f"{v.major}.{v.minor}"
        if m_v_key not in m:
            m[m_v_key] = []
        m[m_v_key].append(vd)

    res: list[LibraryData] = []

    for k, v_list in m.items():
        last_v = list(sorted(v_list, key=lambda v: v["version"], reverse=True))[0].copy()
        last_v["version"] = Version(k)
        res.append(last_v)

    return sorted(res, key=lambda v: v["version"])


def build_matrix(
    runtime: str, packages: list[str],
    short: bool = True,
    with_eol: bool = False
) -> MatrixResultData:
    eol_client = EndOfLifeClient()

    if with_eol:
        live_runtime = [v["name"] for v in eol_client.get_all_versions(runtime)]
    else:
        live_runtime = [v["name"] for v in eol_client.get_active_versions(runtime)]

    matrix_result: MatrixResultData = {"runtimes": {r: {"packages": {}} for r in live_runtime}}

    package_version_map: dict[str, RuntimePackageVersions] = {}

    for p in packages:
        package_version_map[p] = RuntimePackageVersions(runtime_name=runtime, package_name=p)

    for rt in live_runtime:
        for p in packages:
            ppv = package_version_map[p]
            v_list = ppv.get_versions_by_releases(runtime_version=rt)
            if not with_eol:
                v_list = ppv.remove_eol_versions(v_list)
            if short:
                v_list = deduplicate_versions(v_list)
            matrix_result["runtimes"][rt]["packages"][p] = v_list

    return matrix_result
