
from eol_matrix.matrix import build_matrix


def test_matrix():
    matrix = build_matrix("python", ["django"])
    assert matrix == {}


def test_matrix_pytest():
    matrix = build_matrix("python", ["pytest"])
    assert matrix == {}
