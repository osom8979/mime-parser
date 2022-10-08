# -*- coding: utf-8 -*-

from typing import Final

PLUGIN_PREFIX_ENV_NAME: Final[str] = "MIME_PARSER_PLUGIN_PREFIX"
PLUGIN_DENIES_ENV_NAME: Final[str] = "MIME_PARSER_PLUGIN_DENIES"
PLUGIN_ALLOWS_ENV_NAME: Final[str] = "MIME_PARSER_PLUGIN_ALLOWS"
DISABLE_ORJSON_INSTALL_ENV_NAME: Final[str] = "MIME_PARSER_DISABLE_ORJSON_INSTALL"

ENV_SEPARATOR: Final[str] = ":"

DEFAULT_PLUGIN_PREFIX: Final[str] = "mime-parser-"

PLUGIN_ROOT_ATTR: Final[str] = "__mimes__"
PLUGIN_MIME_ATTR: Final[str] = "mime"
PLUGIN_ENCODER_ATTR: Final[str] = "encoder"
PLUGIN_DECODER_ATTR: Final[str] = "decoder"
