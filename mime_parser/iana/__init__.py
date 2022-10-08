# -*- coding: utf-8 -*-

# Download media types:
# https://www.iana.org/assignments/media-types/media-types.xhtml

import os
from functools import lru_cache
from typing import Dict, Final, List

from mime_parser.mime_type import MimeType

IANA_CSV_ENCODING: Final[str] = "utf-8"
FIRST_LINE_IS_COLUMN_HEADER: Final[bool] = True
"""
The first line is the column header. Probably `Name,Template,Reference`.
"""

IANA_CSV_START_LINE: Final[int] = 1 if FIRST_LINE_IS_COLUMN_HEADER else 0

TYPE_APPLICATION = "application"
TYPE_AUDIO = "audio"
TYPE_FONT = "font"
TYPE_EXAMPLE = "example"
TYPE_IMAGE = "image"
TYPE_MESSAGE = "message"
TYPE_MODEL = "model"
TYPE_MULTIPART = "multipart"
TYPE_TEXT = "text"
TYPE_VIDEO = "video"

REGISTERED_TYPES = (
    TYPE_APPLICATION,
    TYPE_AUDIO,
    TYPE_FONT,
    TYPE_EXAMPLE,
    TYPE_IMAGE,
    TYPE_MESSAGE,
    TYPE_MODEL,
    TYPE_MULTIPART,
    TYPE_TEXT,
    TYPE_VIDEO,
)


def read_iana_csv_mimes(
    path: str,
    encoding=IANA_CSV_ENCODING,
    start_line=IANA_CSV_START_LINE,
) -> List[MimeType]:
    result = list()
    with open(path, "r", encoding=encoding) as f:
        for line in f.readlines()[start_line:]:
            items = line.split(",")
            if len(items) != 3:
                continue

            name = items[0].strip()
            template = items[1].strip()
            reference = items[2].strip()
            try:
                result.append(MimeType.parse(template, name, reference))
            except:  # noqa
                continue
    return result


def read_iana_csv_mimes_with_type_name(type_name: str) -> List[MimeType]:
    iana_directory = os.path.dirname(__file__)
    csv_path = os.path.join(iana_directory, f"{type_name}.csv")
    try:
        return read_iana_csv_mimes(csv_path)
    except BaseException as e:  # noqa
        return list()


@lru_cache
def registered_mime_types() -> Dict[str, List[MimeType]]:
    return {t: read_iana_csv_mimes_with_type_name(t) for t in REGISTERED_TYPES}
