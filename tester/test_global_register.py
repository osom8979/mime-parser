# -*- coding: utf-8 -*-

from json import loads
from unittest import TestCase, main

from mime_parser.global_register import decode, encode


class GlobalRegisterTestCase(TestCase):
    def test_default(self):
        test_mime = "application/json"
        test_data = {"num": 100, "bool": True}

        encoded_data = encode(test_mime, test_data)
        self.assertIsInstance(encoded_data, bytes)

        decoded_data = decode(test_mime, encoded_data)
        self.assertDictEqual(test_data, decoded_data)
        self.assertDictEqual(loads(encoded_data), decoded_data)


if __name__ == "__main__":
    main()
