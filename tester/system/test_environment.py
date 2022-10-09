# -*- coding: utf-8 -*-

from unittest import TestCase, main

from mime_parser.system.environment import (
    get_plugin_allows,
    get_plugin_denies,
    get_plugin_prefix,
)
from mime_parser.system.environment_context import EnvironmentContext
from mime_parser.variables import (
    PLUGIN_ALLOWS_ENV_NAME,
    PLUGIN_DENIES_ENV_NAME,
    PLUGIN_PREFIX_ENV_NAME,
)


class EnvironmentTestCase(TestCase):
    def setUp(self):
        self.exchanges = {
            PLUGIN_ALLOWS_ENV_NAME: "A:B:C",
            PLUGIN_DENIES_ENV_NAME: "D:E:F",
            PLUGIN_PREFIX_ENV_NAME: "PREFIX",
        }
        self.context = EnvironmentContext(**self.exchanges)
        self.context.open()

    def tearDown(self):
        self.context.close()

    def test_read_os_envs(self):
        allows = get_plugin_allows()
        denies = get_plugin_denies()
        prefix = get_plugin_prefix()

        self.assertListEqual(["A", "B", "C"], allows)
        self.assertListEqual(["D", "E", "F"], denies)
        self.assertEqual("PREFIX", prefix)


if __name__ == "__main__":
    main()
