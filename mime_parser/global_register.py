# -*- coding: utf-8 -*-

from functools import lru_cache
from typing import Any

from mime_parser.codec.json import create_json_codec
from mime_parser.logging import logger
from mime_parser.mime.mime_codec_register import MimeCodecRegister
from mime_parser.pattern.singleton import singleton
from mime_parser.plugin.find_plugin_codecs import find_plugin_codecs


@singleton
class _GlobalMimeCodecRegister(MimeCodecRegister):
    def __init__(self, register_default_json_codec=True, raise_if_errors=True):
        super().__init__()

        # Default codecs
        if register_default_json_codec:
            self.register(create_json_codec())

        codecs = find_plugin_codecs(raise_if_errors=raise_if_errors)
        for codec in codecs:
            logger.debug(f"Register mime codec: {str(codec.mime)}")
            self.register(codec)


@lru_cache
def global_mime_codec_register() -> MimeCodecRegister:
    return _GlobalMimeCodecRegister()


def encode(mime: str, data: Any) -> bytes:
    return global_mime_codec_register().encode(mime, data)


def decode(mime: str, data: bytes) -> Any:
    return global_mime_codec_register().decode(mime, data)
