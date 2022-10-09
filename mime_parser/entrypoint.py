# -*- coding: utf-8 -*-

from typing import Callable, List, Optional

from mime_parser.apps.decode_main import main as decode_main
from mime_parser.apps.encode_main import main as encode_main
from mime_parser.apps.iana_main import main as iana_main
from mime_parser.apps.list_main import main as list_main
from mime_parser.arguments import (
    CMD_DECODE,
    CMD_ENCODE,
    CMD_IANA,
    CMD_LIST,
    CMDS,
    get_default_arguments,
)
from mime_parser.logging import logger
from mime_parser.logging.logging import set_root_level, set_simple_logging_config


def main(
    cmdline: Optional[List[str]] = None,
    printer: Callable[..., None] = print,
) -> int:
    args = get_default_arguments(cmdline)

    if not args.cmd:
        printer("The command does not exist")
        return 1

    cmd = args.cmd
    simple_logging = args.simple_logging
    severity = args.severity
    verbose = args.verbose

    assert cmd in CMDS
    assert isinstance(simple_logging, bool)
    assert isinstance(severity, str)
    assert isinstance(verbose, int)

    if simple_logging:
        set_simple_logging_config()
    set_root_level(severity)

    logger.debug(f"Arguments: {args}")

    try:
        if cmd == CMD_IANA:
            return iana_main(args, printer=printer)
        elif cmd == CMD_LIST:
            return list_main(args, printer=printer)
        elif cmd == CMD_ENCODE:
            return encode_main(args)
        elif cmd == CMD_DECODE:
            return decode_main(args)
        else:
            assert False, "Inaccessible section"
    except BaseException as e:
        logger.exception(e)
        return 1


if __name__ == "__main__":
    exit(main())
