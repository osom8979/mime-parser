# -*- coding: utf-8 -*-

from mime_parser.global_register import decode, encode, register, unregister
from mime_parser.iana.registered_mime_types import registered_mime_types
from mime_parser.mime.mime_codec import MimeCodec
from mime_parser.mime.mime_type import MimeType, parse_mime

__version__ = "1.2.0"

__all__ = (
    "MimeCodec",
    "MimeType",
    "__version__",
    "decode",
    "encode",
    "parse_mime",
    "register",
    "registered_mime_types",
    "unregister",
)
