from eol_matrix.runtimes.python import PythonVersion
from packaging.specifiers import SpecifierSet


def test_get_runtime_version():
    p_v = PythonVersion()
    assert p_v.get_runtime_version("django", "6.0") == SpecifierSet(">=3.12")


def test_get_package_versions():
    p_v = PythonVersion()
    assert p_v.get_package_versions("xlsx2html") == []
