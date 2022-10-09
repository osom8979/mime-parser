# -*- coding: utf-8 -*-

from json import dumps, loads
from typing import Any
from unittest import TestCase, main

from mime_parser.mime.mime_codec import MimeCodec


def json_encoder(value: Any) -> bytes:
    return bytes(dumps(value), encoding="utf-8")


def json_decoder(value: bytes) -> Any:
    return loads(value)


class MimeCodecTestCase(TestCase):
    def setUp(self):
        self.codec = MimeCodec("application/json")
        self.assertFalse(self.codec.has_encoder())
        self.assertFalse(self.codec.has_decoder())
        self.codec.set_encoder(json_encoder)
        self.codec.set_decoder(json_decoder)
        self.assertTrue(self.codec.has_encoder())
        self.assertTrue(self.codec.has_decoder())

    def tearDown(self):
        self.assertTrue(self.codec.has_encoder())
        self.assertTrue(self.codec.has_decoder())
        self.codec.remove_encoder()
        self.codec.remove_decoder()
        self.assertFalse(self.codec.has_encoder())
        self.assertFalse(self.codec.has_decoder())

    def test_default(self):
        test_data = {"aa": 11, "bb": 22.5, "cc": [1, 2, 3]}
        encoded_data = self.codec.encode(test_data)
        self.assertIsInstance(encoded_data, bytes)

        decoded_data = self.codec.decode(encoded_data)
        self.assertIsInstance(decoded_data, dict)
        self.assertEqual(decoded_data, test_data)


if __name__ == "__main__":
    main()
