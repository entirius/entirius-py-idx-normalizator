# entirius-py-idx-normalizator

Normalizers and validators for product identifiers, part of Entirius, the open-source modular ecommerce platform. It
covers the index (`idx`: slugified, length-capped with an md5 suffix), the SKU, the EAN and the URL key.

[![PyPI](https://img.shields.io/pypi/v/entirius-py-idx-normalizator.svg)](https://pypi.org/project/entirius-py-idx-normalizator/)
[![Python](https://img.shields.io/pypi/pyversions/entirius-py-idx-normalizator.svg)](https://pypi.org/project/entirius-py-idx-normalizator/)
[![License: MPL-2.0](https://img.shields.io/badge/license-MPL--2.0-blue.svg)](https://github.com/entirius/entirius-py-idx-normalizator/blob/develop/LICENSE)

## What it does

- Slugifies a text into an index and caps it at `max_len` with a short hash suffix (`normalize_idx()`).
- Strips a SKU (`normalize_sku()`) and rejects commas and out-of-range lengths (`validate_sku()`).
- Lower-cases and strips an EAN (`normalize_ean()`) and checks its length (`validate_ean()`).
- Slugifies a URL key (`normalize_url_key()`, `validate_url_key()`).
- Every `validate_*` function raises on a value that is not in its normalized form.

## Installation

```shell
uv add entirius-py-idx-normalizator
pip install entirius-py-idx-normalizator
```

The import name is `idx_normalizator`.

## Quick start

```python
from idx_normalizator import normalize_idx, validate_idx, validate_sku, normalize_ean

normalize_idx("Example Cammel Name")   # "example-cammel-name"
validate_idx("example-cammel-name")    # raises ValueError if not a valid idx
validate_sku("ABC-123")                # raises ValueError on forbidden chars / length
normalize_ean(" 5901234 ")             # "5901234"
```

## Requirements

- Python 3.11 or newer.
- `python-slugify` (installed as a dependency).

## Documentation

- Entirius documentation: https://docs.entirius.com/
- Changelog: https://github.com/entirius/entirius-py-idx-normalizator/blob/develop/CHANGELOG.md

## Part of Entirius

This library keeps product identifiers consistent across the Entirius backend service (Volkanos) and its modules.

- Backend service: https://github.com/entirius/entirius-service-volkanos
- Docker harness: https://github.com/entirius/entirius-zeno
- Consumer modules: https://github.com/entirius/entirius-django-pim, https://github.com/entirius/entirius-django-utils, https://github.com/entirius/entirius-django-checkout

## Development

```shell
make install     # sync dependencies (uv)
make check       # lint + format check (ruff)
make test        # test suite (pytest)
```

Development and agent instructions: https://github.com/entirius/entirius-py-idx-normalizator/blob/develop/AGENTS.md

## License

Mozilla Public License 2.0 (MPL-2.0) — see https://github.com/entirius/entirius-py-idx-normalizator/blob/develop/LICENSE.
