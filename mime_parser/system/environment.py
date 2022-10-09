# -*- coding: utf-8 -*-

from os import environ
from typing import List

from mime_parser.variables import (
    DEFAULT_PLUGIN_PREFIX,
    ENV_SEPARATOR,
    PLUGIN_ALLOWS_ENV_NAME,
    PLUGIN_DENIES_ENV_NAME,
    PLUGIN_PREFIX_ENV_NAME,
)


def _split_arguments(value: str, separator=ENV_SEPARATOR) -> List[str]:
    lines0 = value.split(separator)
    lines1 = map(lambda x: x.strip(), lines0)
    lines2 = filter(lambda x: x, lines1)
    return list(lines2)


def get_plugin_allows() -> List[str]:
    if PLUGIN_ALLOWS_ENV_NAME in environ:
        return _split_arguments(environ[PLUGIN_ALLOWS_ENV_NAME])
    else:
        return list()


def get_plugin_denies() -> List[str]:
    if PLUGIN_DENIES_ENV_NAME in environ:
        return _split_arguments(environ[PLUGIN_DENIES_ENV_NAME])
    else:
        return list()


def get_plugin_prefix() -> str:
    if PLUGIN_PREFIX_ENV_NAME in environ:
        return environ[PLUGIN_PREFIX_ENV_NAME]
    else:
        return DEFAULT_PLUGIN_PREFIX
