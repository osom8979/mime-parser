# -*- coding: utf-8 -*-

import os
import sys
from copy import deepcopy
from unittest import TestCase, main

from mime_parser.plugin.find_plugin_codecs import find_plugin_codecs

PLUGIN_DIR = os.path.dirname(__file__)


class FindPluginCodecsTestCase(TestCase):
    def setUp(self):
        self.plugin_dir_exists = PLUGIN_DIR in sys.path
        self.original_sys_path = deepcopy(sys.path)
        if not self.plugin_dir_exists:
            sys.path.insert(0, PLUGIN_DIR)
        self.assertIn(PLUGIN_DIR, sys.path)

    def tearDown(self):
        sys.path = self.original_sys_path  # Restore sys.path
        if self.plugin_dir_exists:
            self.assertIn(PLUGIN_DIR, sys.path)
        else:
            self.assertNotIn(PLUGIN_DIR, sys.path)

    def test_default(self):
        test_mime = "application/test"
        codecs = find_plugin_codecs(prefix="test_")
        self.assertLessEqual(1, len(codecs))

        filtered_codecs = list(filter(lambda x: str(x.mime) == test_mime, codecs))
        self.assertEqual(1, len(filtered_codecs))

        codec = filtered_codecs[0]
        self.assertEqual(test_mime, str(codec.mime))

        original_data = "[TEST_VALUE]"
        encoded_data = codec.encode(original_data)
        self.assertEqual(b"__test_[TEST_VALUE]__", encoded_data)

        decoded_data = codec.decode(encoded_data)
        self.assertEqual(original_data, decoded_data)


if __name__ == "__main__":
    main()
