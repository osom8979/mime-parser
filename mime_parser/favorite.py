# -*- coding: utf-8 -*-

from typing import Final

from mime_parser.mime.mime_type import PARAMETER_SEPARATOR, MimeType, parse_mime

SINGLE_ANY: Final[str] = "*"
BOTH_ANY: Final[str] = "*/*"

APPLICATION_OCTET_STREAM: Final[str] = "application/octet-stream"
APPLICATION_GZIP: Final[str] = "application/gzip"
APPLICATION_JSON: Final[str] = "application/json"
APPLICATION_XML: Final[str] = "application/xml"
APPLICATION_YAML: Final[str] = "application/x-yaml"
APPLICATION_FORM: Final[str] = "application/x-www-form-urlencoded"
TEXT_PLAIN: Final[str] = "text/plain"

CHARSET_UTF8: Final[str] = "charset=utf-8"
APPEND_CHARSET_UTF8: Final[str] = PARAMETER_SEPARATOR + CHARSET_UTF8

APPLICATION_JSON_UTF8: Final[str] = APPLICATION_JSON + APPEND_CHARSET_UTF8
APPLICATION_XML_UTF8: Final[str] = APPLICATION_XML + APPEND_CHARSET_UTF8
APPLICATION_YAML_UTF8: Final[str] = APPLICATION_YAML + APPEND_CHARSET_UTF8
APPLICATION_FORM_UTF8: Final[str] = APPLICATION_FORM + APPEND_CHARSET_UTF8
TEXT_PLAIN_UTF8: Final[str] = TEXT_PLAIN + APPEND_CHARSET_UTF8

MIME_ANY: Final[MimeType] = parse_mime(SINGLE_ANY)
MIME_ANY_BOTH: Final[MimeType] = parse_mime(BOTH_ANY)
MIME_APPLICATION_OCTET_STREAM: Final[MimeType] = parse_mime(APPLICATION_OCTET_STREAM)
MIME_APPLICATION_GZIP: Final[MimeType] = parse_mime(APPLICATION_GZIP)
MIME_APPLICATION_JSON: Final[MimeType] = parse_mime(APPLICATION_JSON)
MIME_APPLICATION_XML: Final[MimeType] = parse_mime(APPLICATION_XML)
MIME_APPLICATION_YAML: Final[MimeType] = parse_mime(APPLICATION_YAML)
MIME_APPLICATION_FORM: Final[MimeType] = parse_mime(APPLICATION_FORM)
MIME_TEXT_PLAIN: Final[MimeType] = parse_mime(TEXT_PLAIN)

MIME_APPLICATION_JSON_UTF8: Final[MimeType] = parse_mime(APPLICATION_JSON_UTF8)
MIME_APPLICATION_XML_UTF8: Final[MimeType] = parse_mime(APPLICATION_XML_UTF8)
MIME_APPLICATION_YAML_UTF8: Final[MimeType] = parse_mime(APPLICATION_YAML_UTF8)
MIME_APPLICATION_FORM_UTF8: Final[MimeType] = parse_mime(APPLICATION_FORM_UTF8)
MIME_TEXT_PLAIN_UTF8: Final[MimeType] = parse_mime(TEXT_PLAIN_UTF8)
