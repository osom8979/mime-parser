# -*- coding: utf-8 -*-

from argparse import ArgumentParser, Namespace, RawDescriptionHelpFormatter
from functools import lru_cache
from typing import Final, List, Optional

from mime_parser.iana.registered_mime_types import REGISTERED_TYPES
from mime_parser.logging.logging import SEVERITIES, SEVERITY_NAME_INFO

PROG: Final[str] = "mime_parser"
DESCRIPTION: Final[str] = "Encodes and decodes MIME data"
EPILOG: Final[str] = ""

DEFAULT_SEVERITY: Final[str] = SEVERITY_NAME_INFO

CMD_IANA = "iana"
CMD_LIST = "list"
CMD_ENCODE = "encode"
CMD_DECODE = "decode"
CMDS = (CMD_IANA, CMD_LIST, CMD_ENCODE, CMD_DECODE)

CMD_IANA_HELP: Final[str] = "Prints the MIME types registered with IANA"
CMD_IANA_EPILOG: Final[str] = ""

CMD_LIST_HELP: Final[str] = "Prints a list of installed codecs"
CMD_LIST_EPILOG: Final[str] = ""

CMD_ENCODE_HELP: Final[str] = "Encodes MIME data"
CMD_ENCODE_EPILOG: Final[str] = ""

CMD_DECODE_HELP: Final[str] = "Decodes MIME data"
CMD_DECODE_EPILOG: Final[str] = ""


@lru_cache
def version() -> str:
    # [IMPORTANT] Avoid 'circular import' issues
    from mime_parser import __version__

    return __version__


def add_cmd_iana_parser(subparsers) -> None:
    # noinspection SpellCheckingInspection
    parser = subparsers.add_parser(
        name=CMD_IANA,
        help=CMD_IANA_HELP,
        formatter_class=RawDescriptionHelpFormatter,
        epilog=CMD_IANA_EPILOG,
    )
    assert isinstance(parser, ArgumentParser)

    parser.add_argument(
        "family",
        default=None,
        choices=REGISTERED_TYPES,
        nargs="?",
        help="Only the entered MIME family type is printed",
    )
    parser.add_argument(
        "--without-template",
        action="store_true",
        default=False,
        help="Suppress the printing of the 'template' attribute",
    )
    parser.add_argument(
        "--without-reference",
        action="store_true",
        default=False,
        help="Suppress the printing of the 'reference' attribute",
    )


def add_cmd_list_parser(subparsers) -> None:
    # noinspection SpellCheckingInspection
    parser = subparsers.add_parser(
        name=CMD_LIST,
        help=CMD_LIST_HELP,
        formatter_class=RawDescriptionHelpFormatter,
        epilog=CMD_LIST_EPILOG,
    )
    assert isinstance(parser, ArgumentParser)

    parser.add_argument(
        "--without-header",
        action="store_true",
        default=False,
        help="Suppress the printing of the header",
    )


def add_cmd_encode_parser(subparsers) -> None:
    # noinspection SpellCheckingInspection
    parser = subparsers.add_parser(
        name=CMD_ENCODE,
        help=CMD_ENCODE_HELP,
        formatter_class=RawDescriptionHelpFormatter,
        epilog=CMD_ENCODE_EPILOG,
    )
    assert isinstance(parser, ArgumentParser)

    parser.add_argument("mime", help="Mime Type")


def add_cmd_decode_parser(subparsers) -> None:
    # noinspection SpellCheckingInspection
    parser = subparsers.add_parser(
        name=CMD_DECODE,
        help=CMD_DECODE_HELP,
        formatter_class=RawDescriptionHelpFormatter,
        epilog=CMD_DECODE_EPILOG,
    )
    assert isinstance(parser, ArgumentParser)

    parser.add_argument("mime", help="Mime Type")


def default_argument_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog=PROG,
        description=DESCRIPTION,
        epilog=EPILOG,
        formatter_class=RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--simple-logging",
        "-s",
        action="store_true",
        default=False,
        help="Use simple logging",
    )
    parser.add_argument(
        "--severity",
        choices=SEVERITIES,
        default=DEFAULT_SEVERITY,
        help=f"Logging severity (default: '{DEFAULT_SEVERITY}')",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="count",
        default=0,
        help="Be more verbose/talkative during the operation",
    )
    parser.add_argument(
        "--version",
        "-V",
        action="version",
        version=version(),
    )

    subparsers = parser.add_subparsers(dest="cmd")
    add_cmd_iana_parser(subparsers)
    add_cmd_list_parser(subparsers)
    add_cmd_encode_parser(subparsers)
    add_cmd_decode_parser(subparsers)
    return parser


def get_default_arguments(
    cmdline: Optional[List[str]] = None,
    namespace: Optional[Namespace] = None,
) -> Namespace:
    parser = default_argument_parser()
    return parser.parse_known_args(cmdline, namespace)[0]
