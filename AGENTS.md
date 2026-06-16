# AGENTS.md

> Руководство для ИИ-агентов, работающих с проектом **eol-matrix**.

## О проекте

**eol-matrix** — утилита для построения матрицы совместимости версий рантайма (например, Python)
и библиотек (например, Django). Данные загружаются с API [endoflife.date](https://endoflife.date)
и PyPI.

## Стек

| Компонент            | Технология                            |
| -------------------- | ------------------------------------- |
| Язык                 | Python >= 3.10                        |
| Менеджер пакетов     | [uv](https://github.com/astral-sh/uv) |
| Сборщик              | setuptools                            |
| HTTP-клиент          | `requests`                            |
| Версионирование      | `packaging`                           |
| Линтер / Форматтер   | [Ruff](https://docs.astral.sh/ruff/)  |
| Типизация            | [mypy](https://mypy.readthedocs.io/)  |
| Тестирование         | [pytest](https://docs.pytest.org/)    |
| Версии               | [bump-my-version](https://github.com/callowayproject/bump-my-version) |

## Структура

```
eol-matrix/
├── AGENTS.md                 # ← этот файл
├── README.md                 # Описание проекта
├── pyproject.toml            # Зависимости (uv)
├── uv.lock                   # Lock-файл uv
├── .gitignore
├── docs/                     # Документация и спецификации
│   ├── api/
│   │   ├── endoflife.date-v1.md
│   │   └── pypi.md
│   └── specs/
│       ├── matrix.py
│       ├── spec_v1.md
│       └── spec_v2.md
├── src/
│   └── eol_matrix/           # Пакет приложения (src-layout)
│       ├── __init__.py
│       ├── main.py             # Точка входа (парсинг CLI через sys.argv)
│       ├── endoflife_client.py # Клиент API endoflife.date
│       ├── py.typed
│       ├── cli/
│       │   ├── __init__.py
│       │   └── matrix.py
│       └── runtimes/
│           ├── __init__.py
│           ├── base.py         # Базовый класс рантайма
│           └── python.py
└── tests/                    # Тесты
    ├── test_example.py
    └── endoflife/
        ├── __init__.py
        └── test_endoflife_client.py
```

## Запуск

```bash
# Установка зависимостей
uv sync

# Запуск (через CLI-скрипт)
uvx https://github.com/Apkawa/eol-matrix.git python django

# Локальный запуск
uv run eol-matrix python django
```

Аргументы CLI: первый — название рантайма (например, `python`), второй — название библиотеки (например, `django`).

## Архитектура

### `main.py` — точка входа

- **`build_compatibility_matrix(runtime, lib_name)`** — основная логика построения матрицы.
  1. Загружает активные версии рантайма и библиотеки через `EndOfLifeClient`.
  2. Для каждой версии библиотеки запрашивает `requires_python` из PyPI API.
  3. Сравнивает с доступными версиями рантайма через `packaging.specifiers.SpecifierSet`.
  4. Возвращает словарь `{lib_key: [compatible_runtime_versions]}`.

### `endoflife_client.py` — клиент API endoflife.date

- **`EndOfLifeClient`** — обёртка над REST API.
- **`get_all_versions(product_name)`** — возвращает все версии продукта, отсортированные по версии.
- **`get_active_versions(product_name)`** — фильтрует только активные (не EOL) версии.

### `runtimes/base.py` — базовый класс рантайма

Определяет интерфейс для поиска зависимостей через разные регистры (PyPI, npm и т.д.).

### `runtimes/python.py` — рантайм Python

Реализация специфичной для Python логики (запросы к PyPI).

### `cli/matrix.py` — CLI-команда

Команда для построения матрицы совместимости.

## Конфигурация

### Зависимости

Файл `pyproject.toml`:

- **runtime**: `>=3.10`
- **deps**: `packaging>=26.2`, `requests>=2.34.2`
- **dev**: `bump-my-version>=0.30.0`, `pytest>=8.0.0`, `ruff>=0.9.0`, `pre-commit>=4.0.0`, `mypy>=2.1.0`

### Ruff

- `line-length = 100`, `target-version = "py314"`
- Правила: `E`, `F`, `I`, `W`

### mypy

- Строгий режим (`strict = true`), `show_error_codes = true`

## Рекомендации для ИИ-агентов

1. **Сохраняйте обратную совместимость** — при изменении API `EndOfLifeClient` обновляйте все места использования.
2. **Тайп-хинты** — проект в строгом режиме mypy; при добавлении нового кода используйте аннотации типов.
3. **Тесты** — при изменении логики добавляйте или обновляйте тесты в `tests/`.
4. **Проверяйте diagnostics** после каждого изменения кода.
5. **Документация** — спецификации хранятся в `docs/specs/`, документация API — в `docs/api/`.
6. **Зависимости** — добавляйте через `uv add <package>`, не редактируйте `pyproject.toml` вручную.
8. **Стиль документации** — не использовать эмодзи, быть лаконичным.

## Тестирование

```bash
# Запуск всех тестов
uv run pytest

# Запуск с подробным выводом
uv run pytest -v

# Запуск конкретной директории
uv run pytest tests/endoflife
```

## Линтинг и форматирование

```bash
# Проверка (lint)
uv run ruff check

# Форматирование
uv run ruff format
```

## Типизация

```bash
uv run mypy src/eol_matrix/
```

## Версионирование

Проект использует `bump-my-version` для управления версиями.

```bash
# Проверка текущей версии
bump-my-version show bump

# bump (patch, minor, major)
bump-my-version bump patch
```
