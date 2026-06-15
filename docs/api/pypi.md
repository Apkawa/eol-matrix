
Endpoint: `https://pypi.org/pypi/`

## /<package>/<version>/json

Выводит версию. надо учитывать что выводит точное совпадение, а не последнюю в ветке `6.0`

```bash
curl https://pypi.org/pypi/django/6.0/json
```

200 OK

```json
{
  "info": {
    "author": null,
    "author_email": "Django Software Foundation \u003Cfoundation@djangoproject.com\u003E",
    "bugtrack_url": null,
    "classifiers": [
      "Development Status :: 5 - Production/Stable",
      "Environment :: Web Environment",
      "Framework :: Django",
      "Intended Audience :: Developers",
      "Operating System :: OS Independent",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3 :: Only",
      "Programming Language :: Python :: 3.12",
      "Programming Language :: Python :: 3.13",
      "Programming Language :: Python :: 3.14",
      "Topic :: Internet :: WWW/HTTP",
      "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
      "Topic :: Internet :: WWW/HTTP :: WSGI",
      "Topic :: Software Development :: Libraries :: Application Frameworks",
      "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    "description": "...",
    "description_content_type": "text/x-rst",
    "docs_url": null,
    "download_url": null,
    "downloads": {
      "last_day": -1,
      "last_month": -1,
      "last_week": -1
    },
    "dynamic": [
      "License-File"
    ],
    "home_page": null,
    "keywords": null,
    "license": null,
    "license_expression": "BSD-3-Clause",
    "license_files": [
      "LICENSE",
      "LICENSE.python"
    ],
    "maintainer": null,
    "maintainer_email": null,
    "name": "Django",
    "package_url": "https://pypi.org/project/Django/",
    "platform": null,
    "project_url": "https://pypi.org/project/Django/",
    "project_urls": {
      "Documentation": "https://docs.djangoproject.com/",
      "Funding": "https://www.djangoproject.com/fundraising/",
      "Homepage": "https://www.djangoproject.com/",
      "Release notes": "https://docs.djangoproject.com/en/stable/releases/",
      "Source": "https://github.com/django/django",
      "Tracker": "https://code.djangoproject.com/"
    },
    "provides_extra": [
      "argon2",
      "bcrypt"
    ],
    "release_url": "https://pypi.org/project/Django/6.0/",
    "requires_dist": [
      "asgiref>=3.9.1",
      "sqlparse>=0.5.0",
      "tzdata; sys_platform == \"win32\"",
      // "argon2-cffi\u003E=23.1.0; extra == \"argon2\"",
      "bcrypt>=4.1.1; extra == \"bcrypt\""
    ],
    "requires_python": ">=3.12",
    "summary": "A high-level Python web framework that encourages rapid development and clean, pragmatic design.",
    "version": "6.0",
    "yanked": false,
    "yanked_reason": null
  },
  "last_serial": 37677816,
  "ownership": {
    "organization": "django",
    "roles": []
  },
  "urls": [
    {
      "comment_text": null,
      "digests": {
        "blake2b_256": "d7aef19e24789a5ad852670d6885f5480f5e5895576945fcc01817dfd9bc002a",
        "md5": "bcad5a904b0d7b57a4e86e40df39c10c",
        "sha256": "1cc2c7344303bbfb7ba5070487c17f7fc0b7174bbb0a38cebf03c675f5f19b6d"
      },
      "downloads": -1,
      "filename": "django-6.0-py3-none-any.whl",
      "has_sig": false,
      "md5_digest": "bcad5a904b0d7b57a4e86e40df39c10c",
      "packagetype": "bdist_wheel",
      "python_version": "py3",
      "requires_python": "\u003E=3.12",
      "size": 8339181,
      "upload_time": "2025-12-03T16:26:16",
      "upload_time_iso_8601": "2025-12-03T16:26:16.231704Z",
      "url": "https://files.pythonhosted.org/packages/d7/ae/f19e24789a5ad852670d6885f5480f5e5895576945fcc01817dfd9bc002a/django-6.0-py3-none-any.whl",
      "yanked": false,
      "yanked_reason": null
    },
  ],
  "vulnerabilities": [
    {
      "aliases": [
        "BIT-django-2025-13473",
        "CVE-2025-13473",
        "PYSEC-2026-42"
      ],
      "details": "An issue was discovered in 6.0 before 6.0.2, 5.2 before 5.2.11, and 4.2 before 4.2.28.\n\nThe `django.contrib.auth.handlers.modwsgi.check_password()` function for authentication via `mod_wsgi` allows remote attackers to enumerate users via a timing attack. Earlier, unsupported Django series (such as 5.0.x, 4.1.x, and 3.2.x) were not evaluated and may also be affected.\n\nDjango would like to thank Stackered for reporting this issue.",
      "fixed_in": [
        "6.0.2",
        "5.2.11",
        "4.2.28"
      ],
      "id": "GHSA-2mcm-79hx-8fxw",
      "link": "https://osv.dev/vulnerability/GHSA-2mcm-79hx-8fxw",
      "source": "osv",
      "summary": null,
      "withdrawn": null
    }
  ]
}
```


## /<package>/json

Получает последний релиз + список **ВСЕХ** релизов в поле `releases`
На некоторых проектах получается довольно большой json, для django - 500кб


```bash
curl https://pypi.org/pypi/Django/json
```

200 OK
```json
{
  "info": {
    "author": null,
    "author_email": "Django Software Foundation <foundation@djangoproject.com>",
    "bugtrack_url": null,
    "classifiers": [
      "Development Status :: 5 - Production/Stable",
      "Environment :: Web Environment",
      "Framework :: Django",
      "Intended Audience :: Developers",
      "Operating System :: OS Independent",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3 :: Only",
      "Programming Language :: Python :: 3.12",
      "Programming Language :: Python :: 3.13",
      "Programming Language :: Python :: 3.14",
      "Topic :: Internet :: WWW/HTTP",
      "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
      "Topic :: Internet :: WWW/HTTP :: WSGI",
      "Topic :: Software Development :: Libraries :: Application Frameworks",
      "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    "description": "...",
    "description_content_type": "text/x-rst",
    "docs_url": null,
    "download_url": null,
    "downloads": {
      "last_day": -1,
      "last_month": -1,
      "last_week": -1
    },
    "dynamic": [
      "License-File"
    ],
    "home_page": null,
    "keywords": null,
    "license": null,
    "license_expression": "BSD-3-Clause",
    "license_files": [
      "LICENSE",
      "LICENSE.python",
      "AUTHORS"
    ],
    "maintainer": null,
    "maintainer_email": null,
    "name": "Django",
    "package_url": "https://pypi.org/project/Django/",
    "platform": null,
    "project_url": "https://pypi.org/project/Django/",
    "project_urls": {
      "Documentation": "https://docs.djangoproject.com/",
      "Funding": "https://www.djangoproject.com/fundraising/",
      "Homepage": "https://www.djangoproject.com/",
      "Release notes": "https://docs.djangoproject.com/en/stable/releases/",
      "Source": "https://github.com/django/django",
      "Tracker": "https://code.djangoproject.com/"
    },
    "provides_extra": [
      "argon2",
      "bcrypt"
    ],
    "release_url": "https://pypi.org/project/Django/6.0.6/",
    "requires_dist": [
      "asgiref>=3.9.1",
      "sqlparse>=0.5.0",
      "tzdata; sys_platform == \"win32\"",
      "argon2-cffi>=23.1.0; extra == \"argon2\"",
      "bcrypt>=4.1.1; extra == \"bcrypt\""
    ],
    "requires_python": ">=3.12",
    "summary": "A high-level Python web framework that encourages rapid development and clean, pragmatic design.",
    "version": "6.0.6",
    "yanked": false,
    "yanked_reason": null
  },
  "last_serial": 37677816,
  "ownership": {
    "organization": "django",
    "roles": []
  },
  "releases": {
    "6.1a1": [
      {
        "comment_text": null,
        "digests": {
          "blake2b_256": "37db7d4ad06746747ceee4807dc9db16085e1424d7bd9cc8bf7dedf9bba16a93",
          "md5": "30e2acc07a802195e58060789bc2a9e0",
          "sha256": "fc617100cc0db25e8e93cb2ed7be65684787a46cbce26ecf87d217e1c5ae4b98"
        },
        "downloads": -1,
        "filename": "django-6.1a1-py3-none-any.whl",
        "has_sig": false,
        "md5_digest": "30e2acc07a802195e58060789bc2a9e0",
        "packagetype": "bdist_wheel",
        "python_version": "py3",
        "requires_python": ">=3.12",
        "size": 8393399,
        "upload_time": "2026-05-20T19:40:43",
        "upload_time_iso_8601": "2026-05-20T19:40:43.638389Z",
        "url": "https://files.pythonhosted.org/packages/37/db/7d4ad06746747ceee4807dc9db16085e1424d7bd9cc8bf7dedf9bba16a93/django-6.1a1-py3-none-any.whl",
        "yanked": false,
        "yanked_reason": null
      },
      {
        "comment_text": null,
        "digests": {
          "blake2b_256": "9cfcbbccfafecb518bc6e3dd5da753570f55c8e59dd8cb4b8b428db64d91b867",
          "md5": "af5d903cc7f1a52d5a7f9251ab6f5e3f",
          "sha256": "abd3a1ec92cf4817654fd83ab708932b5d2d12a0cec993ea169320682c193ad0"
        },
        "downloads": -1,
        "filename": "django-6.1a1.tar.gz",
        "has_sig": false,
        "md5_digest": "af5d903cc7f1a52d5a7f9251ab6f5e3f",
        "packagetype": "sdist",
        "python_version": "source",
        "requires_python": ">=3.12",
        "size": 11172061,
        "upload_time": "2026-05-20T19:40:50",
        "upload_time_iso_8601": "2026-05-20T19:40:50.995447Z",
        "url": "https://files.pythonhosted.org/packages/9c/fc/bbccfafecb518bc6e3dd5da753570f55c8e59dd8cb4b8b428db64d91b867/django-6.1a1.tar.gz",
        "yanked": false,
        "yanked_reason": null
      }
    ]
  },
  "urls": [
    {
      "comment_text": null,
      "digests": {
        "blake2b_256": "eb5023f9dc45483419a3cc2085b498b25adfbf10642b2941c73e6d2dfaffc9ab",
        "md5": "15a34bf4b721155c67d3079c78c045b2",
        "sha256": "25148b1194c47c2e685e5f5e9c5d59c78b075dfd282cb9618861ba6c1708f4d2"
      },
      "downloads": -1,
      "filename": "django-6.0.6-py3-none-any.whl",
      "has_sig": false,
      "md5_digest": "15a34bf4b721155c67d3079c78c045b2",
      "packagetype": "bdist_wheel",
      "python_version": "py3",
      "requires_python": ">=3.12",
      "size": 8373354,
      "upload_time": "2026-06-03T13:02:41",
      "upload_time_iso_8601": "2026-06-03T13:02:41.720263Z",
      "url": "https://files.pythonhosted.org/packages/eb/50/23f9dc45483419a3cc2085b498b25adfbf10642b2941c73e6d2dfaffc9ab/django-6.0.6-py3-none-any.whl",
      "yanked": false,
      "yanked_reason": null
    },
    {
      "comment_text": null,
      "digests": {
        "blake2b_256": "7829ac41e16097af67066d97a7d5775c5d8e7efc5d0284f6b0a159e07b9adb92",
        "md5": "b45e074d29f85e1417fb2d2ea97c2df3",
        "sha256": "ad03916ba59523d781ae5c3f631960c23d69a9d9c43cecda52fc23b47e953713"
      },
      "downloads": -1,
      "filename": "django-6.0.6.tar.gz",
      "has_sig": false,
      "md5_digest": "b45e074d29f85e1417fb2d2ea97c2df3",
      "packagetype": "sdist",
      "python_version": "source",
      "requires_python": ">=3.12",
      "size": 10905525,
      "upload_time": "2026-06-03T13:02:46",
      "upload_time_iso_8601": "2026-06-03T13:02:46.503360Z",
      "url": "https://files.pythonhosted.org/packages/78/29/ac41e16097af67066d97a7d5775c5d8e7efc5d0284f6b0a159e07b9adb92/django-6.0.6.tar.gz",
      "yanked": false,
      "yanked_reason": null
    }
  ],
  "vulnerabilities": []
}
```
