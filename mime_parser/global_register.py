# -*- coding: utf-8 -*-

from functools import lru_cache
from typing import Any, Optional, Union

from mime_parser import codec as default_codecs
from mime_parser.logging import logger
from mime_parser.mime.mime_codec import MimeCodec, MimeDecoder, MimeEncoder
from mime_parser.mime.mime_codec_register import MimeCodecRegister
from mime_parser.pattern.singleton import singleton
from mime_parser.plugin.find_plugin_codecs import find_plugin_codecs


@singleton
class _GlobalMimeCodecRegister(MimeCodecRegister):
    def __init__(self, register_default_json_codec=True, raise_if_errors=True):
        super().__init__()

        # Default codecs
        if register_default_json_codec:
            for family_name in default_codecs.__all__:
                submodule = getattr(default_codecs, family_name)
                for subtype_name in submodule.__all__:
                    codec_module = getattr(submodule, subtype_name)
                    self.register(getattr(codec_module, "codec"))

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


def register(
    mime: Union[str, MimeCodec],
    encoder: Optional[MimeEncoder] = None,
    decoder: Optional[MimeDecoder] = None,
) -> None:
    if isinstance(mime, MimeCodec):
        if encoder or decoder:
            raise ValueError(
                "When registering a `MimeCodec` instance, "
                "there must be no other arguments"
            )
        global_mime_codec_register().register(mime)
    elif isinstance(mime, str):
        global_mime_codec_register().register(MimeCodec(mime, encoder, decoder))
    else:
        raise TypeError(f"Unsupported mime type: {type(mime).__name__}")


def unregister(codec: Union[str, MimeCodec]) -> None:
    global_mime_codec_register().unregister(codec)
