# idx-normalizator

Normalizers and validators for product identifiers — index/idx (slugified, length-capped
with an md5 suffix), SKU, and EAN.

## Installation

```shell
pip install entirius-py-idx-normalizator
```

## Usage

```python
from idx_normalizator import normalize_idx, validate_idx, validate_sku, normalize_ean

normalize_idx("Example Cammel Name")   # "example-cammel-name"
validate_idx("example-cammel-name")    # raises ValueError if not a valid idx
validate_sku("ABC-123")                # raises ValueError on forbidden chars / length
normalize_ean(" 5901234 ")             # "5901234"
```

## Development

```shell
make install     # sync dependencies (uv)
make check       # lint + format check (ruff)
make test        # test suite (pytest)
```

Development and agent instructions: [AGENTS.md](AGENTS.md).

## License

Mozilla Public License 2.0 — see [LICENSE](LICENSE).
