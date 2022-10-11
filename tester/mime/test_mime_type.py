# -*- coding: utf-8 -*-

from unittest import TestCase, main

from mime_parser.favorite import (
    MIME_ANY,
    MIME_ANY_BOTH,
    MIME_APPLICATION_JSON,
    MIME_APPLICATION_OCTET_STREAM,
    MIME_TEXT_PLAIN,
)
from mime_parser.mime.mime_type import MimeType


class MimeTypeTestCase(TestCase):
    def test_default(self):
        self.assertEqual("application", MIME_APPLICATION_OCTET_STREAM.family)
        self.assertEqual("octet-stream", MIME_APPLICATION_OCTET_STREAM.subtype)

        self.assertEqual("application", MIME_APPLICATION_JSON.family)
        self.assertEqual("json", MIME_APPLICATION_JSON.subtype)

        self.assertEqual("text", MIME_TEXT_PLAIN.family)
        self.assertEqual("plain", MIME_TEXT_PLAIN.subtype)

    def test_accept(self):
        text_any = MimeType.parse("text/*")
        any_plain = MimeType.parse("*/plain")
        self.assertTrue(MIME_TEXT_PLAIN.accepts([text_any]))
        self.assertTrue(MIME_TEXT_PLAIN.accepts([any_plain]))
        self.assertTrue(MIME_TEXT_PLAIN.accepts([MIME_ANY]))
        self.assertTrue(MIME_TEXT_PLAIN.accepts([MIME_ANY_BOTH]))

        text_unknown = MimeType.parse("text/unknown")
        unknown_text = MimeType.parse("unknown/text")
        error_mimes = [text_unknown, text_unknown]
        self.assertFalse(MIME_TEXT_PLAIN.accepts([text_unknown]))
        self.assertFalse(MIME_TEXT_PLAIN.accepts([unknown_text]))
        self.assertFalse(MIME_TEXT_PLAIN.accepts(error_mimes))

        mixed_mimes = [text_unknown, text_unknown, MIME_ANY]
        self.assertTrue(MIME_TEXT_PLAIN.accepts(mixed_mimes))

    def test_parameters(self):
        xml_mime = MimeType.parse("application/xml;q=0.9")
        self.assertEqual("q=0.9", xml_mime.parameter)
        self.assertEqual("q", xml_mime.parameter_tuple[0])
        self.assertEqual("0.9", xml_mime.parameter_tuple[1])

        any_mime = MimeType.parse("*/*;q=0.8")
        self.assertEqual("q=0.8", any_mime.parameter)
        self.assertEqual("q", any_mime.parameter_tuple[0])
        self.assertEqual("0.8", any_mime.parameter_tuple[1])

    def test_multipart_mixed(self):
        mime = MimeType.parse("multipart/mixed; boundary=frontier")
        self.assertEqual("multipart", mime.family)
        self.assertEqual("mixed", mime.subtype)
        self.assertEqual("boundary=frontier", mime.parameter)
        self.assertEqual("boundary", mime.parameter_tuple[0])
        self.assertEqual("frontier", mime.parameter_tuple[1])


if __name__ == "__main__":
    main()
