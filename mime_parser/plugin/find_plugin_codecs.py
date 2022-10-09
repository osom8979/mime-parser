# -*- coding: utf-8 -*-

from importlib import import_module
from typing import Any, Dict, Iterable, List, Optional

from mime_parser.mime.mime_codec import MimeCodec
from mime_parser.package.filter import filter_module_names
from mime_parser.system.environment import (
    get_plugin_allows,
    get_plugin_denies,
    get_plugin_prefix,
)
from mime_parser.variables import (
    PLUGIN_DECODER_ATTR,
    PLUGIN_ENCODER_ATTR,
    PLUGIN_MIME_ATTR,
    PLUGIN_ROOT_ATTR,
)


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


def find_plugin_codecs(
    prefix: Optional[str] = None,
    denies: Optional[List[str]] = None,
    allows: Optional[List[str]] = None,
    raise_if_errors=False,
) -> List[MimeCodec]:
    plugin_prefix = prefix if prefix else get_plugin_prefix()
    plugin_denies = denies if denies else get_plugin_allows()
    plugin_allows = allows if allows else get_plugin_denies()

    module_names = filter_module_names(
        prefix=plugin_prefix,
        denies=plugin_denies,
        allows=plugin_allows,
    )

    result = list()

    for module_name in module_names:
        module = import_module(module_name)
        if not hasattr(module, PLUGIN_ROOT_ATTR):
            continue

        mimes = getattr(module, PLUGIN_ROOT_ATTR)
        if not isinstance(mimes, Iterable):
            continue

        for obj in mimes:
            try:
                result.append(create_mime_codec(obj))
            except:  # noqa
                if raise_if_errors:
                    raise

    return result
