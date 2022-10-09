# -*- coding: utf-8 -*-

from unittest import TestCase, main

from mime_parser.global_register import global_mime_codec_register


class MimeCodecRegisterTestCase(TestCase):
    def setUp(self):
        self.register = global_mime_codec_register()

    def test_application_json(self):
        mime = "application/json"
        test_data = {"aa": 11, "bb": 22.5, "cc": [1, 2, 3]}
        encoded_data = self.register.encode(mime, test_data)
        self.assertIsInstance(encoded_data, bytes)
        decoded_data = self.register.decode(mime, encoded_data)
        self.assertIsInstance(decoded_data, dict)
        self.assertEqual(decoded_data, test_data)


if __name__ == "__main__":
    main()
