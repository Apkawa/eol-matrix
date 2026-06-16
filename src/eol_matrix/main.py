import sys

import requests
from packaging.specifiers import SpecifierSet
from packaging.version import Version

from eol_matrix.endoflife_client import EndOfLifeClient


def get_pypi_python_constraint(package_name, version):
    """
    Шаг 2: Запрашиваем из PyPI ограничение на версию Python для конкретного пакета.
    Возвращает строку вида '>=3.10'
    """
    url = f"https://pypi.org/pypi/{package_name}/{version}/json"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    return data.get("info", {}).get("requires_python")


def build_compatibility_matrix(runtime, lib_name):
    print(f"Get actual {runtime} and {lib_name} from endoflife.date...")
    eol_client = EndOfLifeClient()

    live_runtime = [v["name"] for v in eol_client.get_active_versions(runtime)]
    # TODO если либы нет в eol - то мы сверяемся со всеми версиями либ из репо
    live_lib = [v["name"] for v in eol_client.get_active_versions(lib_name)]

    print(f"  {runtime}: {live_runtime}")
    print(f"  {lib_name}: {live_lib}\n")

    matrix = {}

    # TODO от типа рантайма мы используем разные апи
    print("Check compatibles...")
    for lib_ver in live_lib:
        # Нам нужна конкретная стабильная версия для PyPI, возьмем дефолтную для цикла
        # Например для цикла '5.1' PyPI отдаст метаданные, если запросить '5.1'
        python_constraint = get_pypi_python_constraint(lib_name, lib_ver)

        if not python_constraint:
            # Если точной версии X.Y в PyPI нет, попробуем взять X.Y.0 для теста
            python_constraint = get_pypi_python_constraint(lib_name, f"{lib_ver}.0")

        if python_constraint:
            spec = SpecifierSet(python_constraint)
            # Отсекаем только те версии Python, которые удовлетворяют условию пакета
            compatible_runtime = [py for py in live_runtime if Version(py) in spec]
            matrix[f"{lib_name}{lib_ver.replace('.', '')}"] = compatible_runtime
            print(
                f"  {lib_name} {lib_ver} require {runtime} ({python_constraint}) -> Compatibly with: {compatible_runtime}"
            )
        else:
            print(f"  ❌ Not found {lib_name} {lib_ver}")

    return matrix

def main():
    result_matrix = build_compatibility_matrix(sys.argv[1], sys.argv[2])
    print("\nResult matrix:")
    import json
    print(json.dumps(result_matrix, indent=2))

if __name__ == "__main__":
    main()
