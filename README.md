# eol-matrix

Утилита для построения матрицы совместимости версий рантайма и библиотеки. Данные загружаются с API [endoflife.date](https://endoflife.date) и PyPI.

## Использование

```bash
# Запуск через uvx
uvx https://github.com/Apkawa/eol-matrix.git python django

# Локальный запуск
uv run eol-matrix python django
```

Аргументы CLI: первый — название рантайма (например, `python`), второй — название библиотеки (например, `django`).

## Как это работает

1. Загружает активные версии рантайма и библиотеки через API endoflife.date.
2. Для каждой версии библиотеки запрашивает `requires_python` из PyPI.
3. Сравнивает с доступными версиями рантайма через `packaging.specifiers.SpecifierSet`.

```bash
$ uv run eol-matrix python django
Get actual python and django from endoflife.date...
  python: ['3.10', '3.11', '3.12', '3.13', '3.14']
  django: ['5.2', '6.0']

Check compatibles...
  django 5.2 require python (>=3.10) -> Compatibly with: ['3.10', '3.11', '3.12', '3.13', '3.14']
  django 6.0 require python (>=3.12) -> Compatibly with: ['3.12', '3.13', '3.14']
Result matrix:
  {
    "django52": [
      "3.10",
      "3.11",
      "3.12",
      "3.13",
      "3.14"
    ],
    "django60": [
      "3.12",
      "3.13",
      "3.14"
    ]
  }
```

## Зависимости

- Python >= 3.10
- `packaging`, `requests`
