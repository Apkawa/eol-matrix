from unittest.mock import Mock, patch

import pytest

from eol_matrix.endoflife_client import EndOfLifeClient


@pytest.fixture
def client():
    return EndOfLifeClient()


@pytest.fixture
def sample_releases():
    return {
        "releases": [
            {"name": "1.0", "isEol": True, "codename": None, "label": "Release 1.0",
             "releaseDate": "2023-01-01", "isLts": False, "isEoas": False,
             "isMaintained": False, "latest": {}, "custom": {}},
            {"name": "2.0", "isEol": False, "codename": None, "label": "Release 2.0",
             "releaseDate": "2024-01-01", "isLts": True, "isEoas": False,
             "isMaintained": True, "latest": {}, "custom": {}},
            {"name": "3.0", "isEol": False, "codename": None, "label": "Release 3.0",
             "releaseDate": "2025-01-01", "isLts": False, "isEoas": True,
             "isMaintained": True, "latest": {}, "custom": {}},
        ]
    }


def _make_response(status_code=200, json_data=None):
    resp = Mock()
    resp.status_code = status_code
    resp.json.return_value = {"result": json_data}
    return resp


class TestGetAllVersions:
    @patch("eol_matrix.endoflife_client.requests.get")
    def test_returns_sorted_releases(self, mock_get, client, sample_releases):
        mock_get.return_value = _make_response(json_data=sample_releases)
        result = client.get_all_versions("django")
        names = [v["name"] for v in result]
        assert names == ["1.0", "2.0", "3.0"]

    @patch("eol_matrix.endoflife_client.requests.get")
    def test_empty_response(self, mock_get, client):
        mock_get.return_value = _make_response(json_data={"releases": []})
        result = client.get_all_versions("nonexistent")
        assert result == []


class TestGetActiveVersions:
    @patch("eol_matrix.endoflife_client.requests.get")
    def test_filters_out_eol_versions(self, mock_get, client, sample_releases):
        mock_get.return_value = _make_response(json_data=sample_releases)
        result = client.get_active_versions("django")
        names = [v["name"] for v in result]
        assert names == ["2.0", "3.0"]
        assert all(not v["isEol"] for v in result)
