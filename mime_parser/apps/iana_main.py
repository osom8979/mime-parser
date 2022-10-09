# -*- coding: utf-8 -*-

from argparse import Namespace
from io import StringIO
from typing import Callable

from mime_parser.iana.registered_mime_types import registered_mime_types


def main(args: Namespace, printer: Callable[..., None] = print) -> int:
    assert args is not None
    assert printer is not None

    verbose = args.verbose
    family = args.family
    without_template = args.without_template
    without_reference = args.without_reference
    assert isinstance(verbose, int)
    assert isinstance(family, (type(None), str))
    assert isinstance(without_template, bool)
    assert isinstance(without_reference, bool)

    total_lines = 0

    for registered_type, mimes in registered_mime_types().items():
        if family is not None and registered_type != family:
            continue

        for mime in mimes:
            line = StringIO()
            line.write(mime.name if mime.name else "[EMPTY]")
            if not without_template and mime.original:
                line.write(f": {mime.original}")
            if not without_reference and mime.reference:
                line.write(f" -> {mime.reference}")
            printer(line.getvalue())
            total_lines += 1

    if verbose >= 1:
        printer(f"Total mime-types: {total_lines}")

    return 0
