# -*- coding: utf-8 -*-

import sys
from logging import (
    CRITICAL,
    DEBUG,
    ERROR,
    FATAL,
    INFO,
    NOTSET,
    WARN,
    WARNING,
    Formatter,
    StreamHandler,
    getLogger,
)
from typing import Final, Literal, Optional, Union

SEVERITY_NAME_CRITICAL = "critical"
SEVERITY_NAME_FATAL = "fatal"
SEVERITY_NAME_ERROR = "error"
SEVERITY_NAME_WARNING = "warning"
SEVERITY_NAME_WARN = "warn"
SEVERITY_NAME_INFO = "info"
SEVERITY_NAME_DEBUG = "debug"
SEVERITY_NAME_NOTSET = "notset"
SEVERITY_NAME_OFF = "off"

SEVERITIES = (
    SEVERITY_NAME_CRITICAL,
    SEVERITY_NAME_FATAL,
    SEVERITY_NAME_ERROR,
    SEVERITY_NAME_WARNING,
    SEVERITY_NAME_WARN,
    SEVERITY_NAME_INFO,
    SEVERITY_NAME_DEBUG,
    SEVERITY_NAME_NOTSET,
    SEVERITY_NAME_OFF,
)

LoggingStyleLiteral = Literal["%", "{", "$"]

SIMPLE_LOGGING_FORMAT: Final[str] = "{levelname[0]} [{name}] {message}"
SIMPLE_LOGGING_STYLE: Final[LoggingStyleLiteral] = "{"


def convert_level_number(level: Optional[Union[str, int]] = None) -> int:
    if level is None:
        return DEBUG

    if isinstance(level, str):
        ll = level.lower()
        if ll == SEVERITY_NAME_CRITICAL:
            return CRITICAL
        elif ll == SEVERITY_NAME_FATAL:
            return FATAL
        elif ll == SEVERITY_NAME_ERROR:
            return ERROR
        elif ll == SEVERITY_NAME_WARNING:
            return WARNING
        elif ll == SEVERITY_NAME_WARN:
            return WARN
        elif ll == SEVERITY_NAME_INFO:
            return INFO
        elif ll == SEVERITY_NAME_DEBUG:
            return DEBUG
        elif ll == SEVERITY_NAME_NOTSET:
            return NOTSET
        elif ll == SEVERITY_NAME_OFF:
            return CRITICAL + 100
        else:
            try:
                return int(ll)
            except ValueError:
                raise ValueError(f"Unknown level: {level}")
    elif isinstance(level, int):
        return level
    else:
        raise TypeError(f"Unsupported level type: {type(level)}")


def set_root_level(level: Union[str, int]) -> None:
    getLogger().setLevel(convert_level_number(level))


def set_simple_logging_config() -> None:
    simple_formatter = Formatter(fmt=SIMPLE_LOGGING_FORMAT, style=SIMPLE_LOGGING_STYLE)
    stream_handler = StreamHandler(sys.stdout)
    stream_handler.setFormatter(simple_formatter)
    getLogger().addHandler(stream_handler)
