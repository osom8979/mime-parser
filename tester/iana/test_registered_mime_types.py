# -*- coding: utf-8 -*-

from unittest import TestCase, main

from mime_parser.iana.registered_mime_types import (
    REGISTERED_TYPES,
    TYPE_APPLICATION,
    TYPE_AUDIO,
    TYPE_EXAMPLE,
    TYPE_FONT,
    TYPE_IMAGE,
    TYPE_MESSAGE,
    TYPE_MODEL,
    TYPE_MULTIPART,
    TYPE_TEXT,
    TYPE_VIDEO,
    registered_mime_types,
)


class RegisteredMimeTypesTestCase(TestCase):
    def setUp(self) -> None:
        self.types = registered_mime_types()

    def test_registered_mime_types(self):
        self.assertListEqual(list(REGISTERED_TYPES), list(self.types.keys()))
        self.assertLess(0, len(self.types[TYPE_APPLICATION]))
        self.assertLess(0, len(self.types[TYPE_AUDIO]))
        self.assertLess(0, len(self.types[TYPE_FONT]))
        self.assertEqual(0, len(self.types[TYPE_EXAMPLE]))
        self.assertLess(0, len(self.types[TYPE_IMAGE]))
        self.assertLess(0, len(self.types[TYPE_MESSAGE]))
        self.assertLess(0, len(self.types[TYPE_MODEL]))
        self.assertLess(0, len(self.types[TYPE_MULTIPART]))
        self.assertLess(0, len(self.types[TYPE_TEXT]))
        self.assertLess(0, len(self.types[TYPE_VIDEO]))


if __name__ == "__main__":
    main()
