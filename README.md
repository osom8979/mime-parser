# mime-parser

[![PyPI](https://img.shields.io/pypi/v/mime-parser?style=flat-square)](https://pypi.org/project/mime-parser/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mime-parser?style=flat-square)
[![GitHub](https://img.shields.io/github/license/osom8979/mime-parser?style=flat-square)](https://github.com/osom8979/mime-parser/)

Encodes and decodes MIME data

## Features

- Supported in Python 3.8 and later.
- MIME text parsing
- MIME based encode and decode
- Plugin support
- IANA media types
- No dependencies

## List of pre-implemented codecs

- application/json
- application/gzip

## Installation

```bash
pip install mime-parser
```

If you want to add [orjson](https://github.com/ijl/orjson) support:
```bash
pip install mime-parser[full]
```

## Usage

### MIME text parsing

```python
from mime_parser import parse_mime

mime = parse_mime("image/jpeg;q=0.8")

print(mime.family)  # image
print(mime.subtype)  # jpeg
print(mime.parameter)  # q=0.8
print(mime.original)  # image/jpeg;q=0.8
print(mime.parameter_tuple)  # ('q', '0.8')
```

### MIME based encode and decode

```python
from mime_parser import decode, encode

original_data = b"..."
encoded_data = encode("application/gzip", original_data)

decoded_data = decode("application/gzip", encoded_data)
assert original_data == decoded_data
```

### Register MIME codec

How to register [pyyaml](https://pyyaml.org/):

```python
import yaml
from mime_parser import decode, register

def yaml_encoder(data):
    return yaml.dump(data).encode("utf-8")

def yaml_decoder(data):
    return yaml.full_load(data)

register("application/yaml", encoder=yaml_encoder, decoder=yaml_decoder)

test_yaml = """
test:
  value: 0
"""

decoded_yaml = decode("application/yaml", test_yaml.encode(encoding="utf-8"))
print(decoded_yaml)
```

### Plugin support

- Your package name must start with `mime-parser-`.
- Add the `__mime_parser__` attribute to your package's root `__init__.py` file.
  - `__mime_parser__` must be `Iterable`.
  - The Element of `__mime_parser__` must contain:
    - `mime` string
    - `encoder(Any) -> bytes` callable
    - `decoder(bytes) -> Any` callable
- The plugin must be installed with pip or included in `sys.path`

Examples of plugins that support [pyyaml](https://pyyaml.org/):

```python
import yaml

def yaml_encoder(data):
    return yaml.dump(data).encode("utf-8")

def yaml_decoder(data):
    return yaml.full_load(data)

__mime_parser__ = [
    {
        "mime": "application/yaml",
        "encoder": yaml_encoder,
        "decoder": yaml_decoder,
    },
]
```

## Command line usage

Encoding:
```bash
echo "..." | python -m mime_parser encode application/gzip > data
```

Decoding:
```bash
cat data | python -m mime_parser decode application/gzip > original
```

Prints a list of installed codecs:
```bash
python -m mime_parser list
```

Prints the MIME types registered with [IANA](https://www.iana.org/assignments/media-types/media-types.xhtml):
```bash
python -m mime_parser iana
```

More options:
```bash
python -m mime_parser --help
```

## Environment variables

- `MIME_PARSER_PLUGIN_PREFIX`: Package name prefix to search for plugins.
- `MIME_PARSER_PLUGIN_DENIES`: Deny list of plugins separated by `:`.
- `MIME_PARSER_PLUGIN_ALLOWS`: Allow list of plugins separated by `:`.
- `MIME_PARSER_DISABLE_ORJSON_INSTALL`: without using orjson, Use the default json library.

## License

See the [LICENSE](./LICENSE) file for details. In summary,
**mime-parser** is licensed under the **MIT license**.
