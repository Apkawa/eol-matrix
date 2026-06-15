# endoflife API

endoflife.date documents EOL dates and support lifecycles for various products. The endoflife API allows users to discover and query for those products.

## General Notes

### Backward compatibility

The endoflife.date API is designed to be backward compatible, meaning that existing clients should continue to work with new versions of the API as long as your integration:

- keep using the same major API version (`/api/v1`),
- follow the 301 redirects (products, categories or tags may occasionally be renamed),
- allow for new fields to be added in API responses (we may add new fields to support new features),
- allow for new values to be added in enumeration fields (such as the product's category).

### Undocumented attributes

Some APIs may return more data than indicated in the documentation. Do not rely on this undocumented data, there is no guarantee about it.

### API return codes

The endoflife.date API uses standard HTTP return codes.

When making HTTP requests, you can check the success or failure status of your request by using the HTTP Status Codes (i.e. 200). You must not use the HTTP Status Messages or Reason-Phrases (i.e. OK), as they are optional and may not be returned in HTTP responses (see RFC9110 for more information).
The API may return the following HTTP status codes:

- `200` (**OK**): The request was successful, and the response contains the requested data.
- `301` (**Moved Permanently**): The requested resource has been moved to a new URL.

  The response will contain a `Location` header with the new URL.
  This header must be followed by the client to access the resource at its new location.

- `304` (**Not Modified**): The resource has not been modified since the last request,

  and the client can use its cached version.

- `404` (**Not Found**): The requested resource does not exist.

  Note that due to some limitations the body of the response is not JSON, but our HTML error page.
  This is not something we can change at the moment, see [#7922](https://github.com/endoflife-date/endoflife.date/issues/7922).

- `429` (**Too Many Requests**): The client has sent too many requests in a given amount of time.

  The response may contain a `Retry-After` header indicating when the client can retry the request.
  This is to prevent abuse of the API and ensure fair usage for all users.


## `/products/{product}`

```bash
curl -X 'GET' \
  'https://endoflife.date/api/v1/products/django' \
  -H 'accept: application/json'

```
200 OK
```json
{
  "schema_version": "1.2.1",
  "generated_at": "2026-06-15T16:11:40+00:00",
  "last_modified": "2026-06-03T18:02:01+00:00",
  "result": {
    "name": "django",
    "aliases": [],
    "label": "Django",
    "category": "framework",
    "tags": [
      "framework",
      "python-runtime"
    ],
    "versionCommand": "python -c \"import django; print(django.get_version())\"",
    "identifiers": [
      {
        "type": "repology",
        "id": "python:django"
      },
      {
        "type": "purl",
        "id": "pkg:github/django/django"
      },
      {
        "type": "purl",
        "id": "pkg:pypi/django"
      },
      {
        "type": "cpe",
        "id": "cpe:2.3:a:djangoproject:django"
      },
      {
        "type": "cpe",
        "id": "cpe:/a:djangoproject:django"
      }
    ],
    "labels": {
      "eoas": "Active Support",
      "discontinued": null,
      "eol": "Security Support",
      "eoes": null
    },
    "links": {
      "icon": "https://cdn.jsdelivr.net/npm/simple-icons/icons/django.svg",
      "html": "https://endoflife.date/django",
      "releasePolicy": "https://www.djangoproject.com/download/#supported-versions"
    },
    "releases": [
      {
        "name": "6.0",
        "codename": null,
        "label": "6.0",
        "releaseDate": "2025-12-03",
        "isLts": false,
        "ltsFrom": null,
        "isEoas": false,
        "eoasFrom": "2026-08-31",
        "isEol": false,
        "eolFrom": "2027-04-30",
        "isMaintained": true,
        "latest": {
          "name": "6.0.6",
          "date": "2026-06-03",
          "link": "https://docs.djangoproject.com/en/6.0/releases/6.0.6/"
        },
        "custom": {
          "supportedPythonVersions": "3.12 - 3.14"
        }
      },
      {
        "name": "5.2",
        "codename": null,
        "label": "5.2 (LTS)",
        "releaseDate": "2025-04-02",
        "isLts": true,
        "ltsFrom": null,
        "isEoas": true,
        "eoasFrom": "2025-12-03",
        "isEol": false,
        "eolFrom": "2028-04-30",
        "isMaintained": true,
        "latest": {
          "name": "5.2.15",
          "date": "2026-06-03",
          "link": "https://docs.djangoproject.com/en/5.2/releases/5.2.15/"
        },
        "custom": {
          "supportedPythonVersions": "3.10 - 3.14 (added in 5.2.8)"
        }
      },
      {
        "name": "5.1",
        "codename": null,
        "label": "5.1",
        "releaseDate": "2024-08-07",
        "isLts": false,
        "ltsFrom": null,
        "isEoas": true,
        "eoasFrom": "2025-04-02",
        "isEol": true,
        "eolFrom": "2025-12-03",
        "isMaintained": false,
        "latest": {
          "name": "5.1.15",
          "date": "2025-12-02",
          "link": "https://docs.djangoproject.com/en/5.1/releases/5.1.15/"
        },
        "custom": {
          "supportedPythonVersions": "3.10 - 3.13 (added in 5.1.3)"
        }
      },
      {
        "name": "5.0",
        "codename": null,
        "label": "5.0",
        "releaseDate": "2023-12-04",
        "isLts": false,
        "ltsFrom": null,
        "isEoas": true,
        "eoasFrom": "2024-08-07",
        "isEol": true,
        "eolFrom": "2025-04-02",
        "isMaintained": false,
        "latest": {
          "name": "5.0.14",
          "date": "2025-04-02",
          "link": "https://docs.djangoproject.com/en/5.0/releases/5.0.14/"
        },
        "custom": {
          "supportedPythonVersions": "3.10 - 3.12"
        }
      }
    ]
  }
}
```


### /products

List all the products referenced on endoflife.date. Only a summary of each product is returned by this endpoint.



```bash
curl -X 'GET' \
  'https://endoflife.date/api/v1/products' \
  -H 'accept: application/json'
```

200 OK
```json
{
  "schema_version": "1.0.0",
  "generated_at": "2023-03-01T14:05:52+01:00",
  "total": 200,
  "result": [
    {
      "name": "ubuntu",
      "label": "Ubuntu",
      "aliases": [
        "ubuntu-linux"
      ],
      "category": "os",
      "tags": [
        "canonical",
        "os"
      ],
      "uri": "https://endoflife.date/api/v1/products/ubuntu/"
    }
  ]
}
```

### /products/full

List all the products referenced on endoflife.date, with all their details. The full products data is returned by this endpoint, making the result a dump of nearly all endoflife.date data. Preferably, use the /products endpoint to get a summary of the products and reduce the amount of data transferred.


```bash
curl -X 'GET' \
  'https://endoflife.date/api/v1/products/full' \
  -H 'accept: application/json'
```

```json
{
  "schema_version": "1.0.0",
  "generated_at": "2023-03-01T14:05:52+01:00",
  "total": 200,
  "result": [
    {
      "name": "ubuntu",
      "label": "Ubuntu",
      "aliases": [
        "ubuntu-linux"
      ],
      "category": "os",
      "tags": [
        "canonical",
        "os"
      ],
      "versionCommand": "lsb_release --release",
      "identifiers": [
        {
          "id": "cpe:/o:canonical:ubuntu_linux",
          "type": "cpe"
        }
      ],
      "labels": {
        "eoas": "Hardware & Maintenance",
        "discontinued": "Discontinued",
        "eol": "Maintenance & Security Support",
        "eoes": "Extended Security Maintenance"
      },
      "links": {
        "icon": "https://simpleicons.org/icons/ubuntu.svg",
        "html": "https://endoflife.date/ubuntu",
        "releasePolicy": "https://wiki.ubuntu.com/Releases"
      },
      "releases": [
        {
          "name": "22.04",
          "codename": "Jammy Jellyfish",
          "label": "22.04 'Jammy Jellyfish' (LTS)",
          "releaseDate": "2022-04-21",
          "isLts": true,
          "ltsFrom": "2022-04-21",
          "isEoas": false,
          "eoasFrom": "2024-09-30",
          "isEol": false,
          "eolFrom": "2027-04-01",
          "isDiscontinued": false,
          "discontinuedFrom": "2027-04-01",
          "isEoes": true,
          "eoesFrom": "2032-04-09",
          "isMaintained": true,
          "latest": {
            "name": "22.04.2",
            "date": "2022-04-21",
            "link": "https://wiki.ubuntu.com/JammyJellyfish/ReleaseNotes/"
          },
          "custom": {
            "chromeVersion": "M136",
            "nodeVersion": "22.15"
          }
        }
      ]
    }
  ]
}
```
