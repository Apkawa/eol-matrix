import sys

from eol_matrix.matrix import build_matrix
import requests
from packaging.specifiers import SpecifierSet
from packaging.version import Version

from eol_matrix.endoflife_client import EndOfLifeClient



def build_compatibility_matrix(runtime: str, lib_names: list[str]):
    matrix = build_matrix(runtime=runtime, packages=lib_names)

    live_runtime = list(matrix['runtimes'].keys())
    print("Check compatibles...")
    print(f"{runtime}: {live_runtime}")
    for runtime_ver, runtime_info in matrix['runtimes'].items():
        print(
            f"  {runtime}-{runtime_ver}:"
        )
        for p_name, p_versions in runtime_info['packages'].items():
            _versions = ', '.join([str(v['version']) for v in p_versions])
            print(
                f"    {p_name}: {_versions}"
            )

    return matrix

def main():
    build_compatibility_matrix(sys.argv[1], sys.argv[2:])
    # print("\nResult matrix:")
    # import json
    # print(json.dumps(result_matrix, indent=2))

if __name__ == "__main__":
    main()
