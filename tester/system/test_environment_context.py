# -*- coding: utf-8 -*-

from os import environ
from unittest import TestCase, main

from mime_parser.system.environment_context import EnvironmentContext


class EnvironmentContextTestCase(TestCase):
    def test_read_os_envs(self):
        original_path = environ.get("PATH")
        test_path = "TEST_PATH"
        with EnvironmentContext(PATH=test_path):
            self.assertEqual(test_path, environ.get("PATH"))
        self.assertEqual(original_path, environ.get("PATH"))


if __name__ == "__main__":
    main()
