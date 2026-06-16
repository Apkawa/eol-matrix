# /// script
# dependencies = [
#   "requests",
#   "packaging",
# ]
# ///
import requests
from packaging.specifiers import SpecifierSet
from packaging.version import Version

def get_active_versions_from_eol(product_name):
    """
    Шаг 1: Берем из endoflife.date только поддерживаемые версии.
    Возвращает список мажорных версий, например: ['3.10', '3.11', '3.12', '3.13']
    """
    url = f"https://endoflife.date/api/v1/products/{product_name}"
    response = requests.get(url)
    if response.status_code != 200:
        return []

    data = response.json()['result']
    # print(data)
    active_versions = []

    for release in data['releases']:
        # Проверяем, что цикл поддержки еще не закончен (eol равен False или дата в будущем)
        # Для простоты смотрим на флаг eol (если строка — значит дата окончания поддержки уже известна/прошла)
        # Но endoflife.date возвращает false, если версия еще поддерживается.
        if release.get('isEol') is False:
            active_versions.append(release['name'])

    return sorted(active_versions, key=Version)

def get_pypi_python_constraint(package_name, version):
    """
    Шаг 2: Запрашиваем из PyPI ограничение на версию Python для конкретного пакета.
    Возвращает строку вида '>=3.10'
    """
    url = f"https://pypi.org/pypi/{package_name}/{version}/json"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    data = response.json()
    return data.get('info', {}).get('requires_python')

def build_compatibility_matrix():
    print("🤖 Шаг 1: Получаем живые версии Python и Django из endoflife.date...")
    live_pythons = get_active_versions_from_eol('python')
    live_djangos = get_active_versions_from_eol('django')

    print(f"  Актуальные Python: {live_pythons}")
    print(f"  Актуальные Django: {live_djangos}\n")

    matrix = {}

    print("🤖 Шаг 2: Проверяем совместимость через PyPI API...")
    for django_ver in live_djangos:
        # Нам нужна конкретная стабильная версия для PyPI, возьмем дефолтную для цикла
        # Например для цикла '5.1' PyPI отдаст метаданные, если запросить '5.1'
        python_constraint = get_pypi_python_constraint('Django', django_ver)

        if not python_constraint:
            # Если точной версии X.Y в PyPI нет, попробуем взять X.Y.0 для теста
            python_constraint = get_pypi_python_constraint('Django', f"{django_ver}.0")

        if python_constraint:
            spec = SpecifierSet(python_constraint)
            # Отсекаем только те версии Python, которые удовлетворяют условию пакета
            compatible_pythons = [py for py in live_pythons if Version(py) in spec]
            matrix[f"django{django_ver.replace('.', '')}"] = compatible_pythons
            print(f"  Django {django_ver} требует Python ({python_constraint}) -> Совместим с: {compatible_pythons}")
        else:
            print(f"  ❌ Не удалось найти метаданные для Django {django_ver} на PyPI")

    return matrix

if __name__ == "__main__":
    result_matrix = build_compatibility_matrix()
    print("\n✅ Итоговая чистая матрица для передачи в ЛЛМ:")
    import json
    print(json.dumps(result_matrix, indent=2))
