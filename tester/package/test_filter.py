# -*- coding: utf-8 -*-

from unittest import TestCase, main

from mime_parser.package.filter import filter_module_names


class FilterTestCase(TestCase):
    def test_filter_module_names(self):
        names1 = filter_module_names(prefix="setup")
        self.assertIn("setuptools", names1)

        names2 = filter_module_names("setup", denies=[r".*tool.*"])
        self.assertNotIn("setuptools", names2)

        names3 = filter_module_names("setup", allows=[r"NO_ANY"])
        self.assertNotIn("setuptools", names3)


if __name__ == "__main__":
    main()
