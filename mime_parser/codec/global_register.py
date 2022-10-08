# -*- coding: utf-8 -*-

from functools import lru_cache
from importlib import import_module
from os import environ
from typing import Any, Dict, Iterable, List

from mime_parser.codec.codecs.json import create_json_codec
from mime_parser.codec.mime_codec import MimeCodec
from mime_parser.codec.mime_codec_register import MimeCodecRegister
from mime_parser.logging import logger
from mime_parser.package.package_utils import filter_module_names
from mime_parser.pattern.singleton import singleton
from mime_parser.variables import (
    DEFAULT_PLUGIN_PREFIX,
    ENV_SEPARATOR,
    PLUGIN_ALLOWS_ENV_NAME,
    PLUGIN_DECODER_ATTR,
    PLUGIN_DENIES_ENV_NAME,
    PLUGIN_ENCODER_ATTR,
    PLUGIN_MIME_ATTR,
    PLUGIN_PREFIX_ENV_NAME,
    PLUGIN_ROOT_ATTR,
)


def _split_arguments(value: str) -> List[str]:
    lines0 = value.split(ENV_SEPARATOR)
    lines1 = map(lambda x: x.strip(), lines0)
    lines2 = filter(lambda x: x and not x.startswith("#"), lines1)
    return list(lines2)


def get_plugin_allows() -> List[str]:
    if PLUGIN_ALLOWS_ENV_NAME in environ:
        return _split_arguments(environ[PLUGIN_ALLOWS_ENV_NAME])
    else:
        return list()


def get_plugin_denies() -> List[str]:
    if PLUGIN_DENIES_ENV_NAME in environ:
        return _split_arguments(environ[PLUGIN_DENIES_ENV_NAME])
    else:
        return list()


def get_plugin_prefix() -> str:
    if PLUGIN_PREFIX_ENV_NAME in environ:
        return environ[PLUGIN_PREFIX_ENV_NAME]
    else:
        return DEFAULT_PLUGIN_PREFIX


def create_mime_codec_with_dict(obj: Dict[str, Any]) -> MimeCodec:
    if PLUGIN_MIME_ATTR not in obj:
        raise KeyError(f"Key '{PLUGIN_MIME_ATTR}' does not exist")

    mime = obj[PLUGIN_MIME_ATTR]
    if not mime:
        raise ValueError("Empty mime value")

    encoder = obj.get(PLUGIN_ENCODER_ATTR, None)
    decoder = obj.get(PLUGIN_DECODER_ATTR, None)
    return MimeCodec(mime=mime, encoder=encoder, decoder=decoder)


def create_mime_codec_with_object(obj: object) -> MimeCodec:
    if not hasattr(obj, PLUGIN_MIME_ATTR):
        raise AttributeError(f"Attribute '{PLUGIN_MIME_ATTR}' does not exist")

    mime = getattr(obj, PLUGIN_MIME_ATTR)
    if not mime:
        raise ValueError("Empty mime value")

    encoder = getattr(obj, PLUGIN_ENCODER_ATTR, None)
    decoder = getattr(obj, PLUGIN_DECODER_ATTR, None)
    return MimeCodec(mime=mime, encoder=encoder, decoder=decoder)


def create_mime_codec(obj: object) -> MimeCodec:
    if isinstance(obj, dict):
        return create_mime_codec_with_dict(obj)
    else:
        return create_mime_codec_with_object(obj)


@singleton
class _GlobalMimeCodecRegister(MimeCodecRegister):
    def __init__(self):
        super().__init__()

        # Default codecs
        self.register(create_json_codec())

        module_names = filter_module_names(
            prefix=get_plugin_prefix(),
            denies=get_plugin_allows(),
            allows=get_plugin_denies(),
        )

        for module_name in module_names:
            module = import_module(module_name)
            if not hasattr(module, PLUGIN_ROOT_ATTR):
                continue

            mimes = getattr(module, PLUGIN_ROOT_ATTR)
            if not isinstance(mimes, Iterable):
                continue

            for obj in mimes:
                try:
                    codec = create_mime_codec(obj)
                    logger.debug(f"Register mime codec: {str(codec.mime)}")
                    self.register(codec)
                except BaseException as e:
                    logger.error(f"Register mime codec error: {e}")


@lru_cache
def global_mime_codec_register() -> MimeCodecRegister:
    return _GlobalMimeCodecRegister()


def encode(mime: str, data: Any) -> bytes:
    return global_mime_codec_register().encode(mime, data)


def decode(mime: str, data: bytes) -> Any:
    return global_mime_codec_register().decode(mime, data)
