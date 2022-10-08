# -*- coding: utf-8 -*-

from mime_parser.codec.mime_codec import MimeCodec
from mime_parser.driver.json import global_json_byte_decoder, global_json_byte_encoder
from mime_parser.favorite import APPLICATION_JSON


def create_json_codec() -> MimeCodec:
    return MimeCodec(
        mime=APPLICATION_JSON,
        encoder=global_json_byte_encoder,
        decoder=global_json_byte_decoder,
    )
