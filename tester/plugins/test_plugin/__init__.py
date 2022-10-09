# -*- coding: utf-8 -*-

from typing import Any

TEST_PREFIX = "__test_"
TEST_SUFFIX = "__"


def test_encoder(data: Any) -> bytes:
    return bytes(f"{TEST_PREFIX}{data}{TEST_SUFFIX}", encoding="utf-8")


def test_decoder(data: bytes) -> Any:
    begin = len(TEST_PREFIX)
    end = -len(TEST_SUFFIX)
    return str(data, encoding="utf-8")[begin:end]


__mime_parser__ = [
    {
        "mime": "application/test",
        "encoder": test_encoder,
        "decoder": test_decoder,
    }
]
