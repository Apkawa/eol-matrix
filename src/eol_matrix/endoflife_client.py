from urllib.parse import urljoin

import requests
from packaging.specifiers import SpecifierSet
from packaging.version import Version


from typing import TypedDict, NotRequired

class ReleaseData(TypedDict):
    name: str
    codename: NotRequired[str | None]
    label: str
    releaseDate: str
    isLts: bool
    ltsFrom: NotRequired[str | None]
    isEoas: bool
    eoasFrom: NotRequired[str | None]
    isEol: bool
    eolFrom: NotRequired[str | None]
    isMaintained: bool
    latest: dict[str, str]
    custom: dict[str, str]


class ProductResponse(TypedDict):
    releases: list[ReleaseData]


class EndOfLifeClient:
    endpoint = f"https://endoflife.date/api/v1/"

    def _request(self, url) -> ProductResponse:
        url = urljoin(self.endpoint, url)
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()["result"]
        return data

    def get_all_versions(self, product_name: str) -> list[ReleaseData]:
        data = self._request(f"products/{product_name}")
        # print(data)
        active_versions = []

        for release in data["releases"]:
            active_versions.append(release)

        return sorted(active_versions, key=lambda k: Version(k['name']))

    def get_active_versions(self, product_name: str) -> list[ReleaseData]:
        versions = self.get_all_versions(product_name)
        return [v for v in versions if v["isEol"] is False]
