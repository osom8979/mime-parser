# -*- coding: utf-8 -*-

from argparse import Namespace
from io import StringIO
from typing import Callable

from mime_parser.global_register import global_mime_codec_register


def main(args: Namespace, printer: Callable[..., None] = print) -> int:
    assert args is not None
    assert printer is not None

    verbose = args.verbose
    without_header = args.without_header
    assert isinstance(verbose, int)
    assert isinstance(without_header, int)

    if not without_header:
        printer("E. = Encoding supported")
        printer(".D = Decoding supported")
        printer("---+-------------------")

    total_lines = 0

    codecs = global_mime_codec_register()
    for mime, codec in codecs.items():
        line = StringIO()
        e = "E" if codec.has_encoder() else "."
        d = "D" if codec.has_decoder() else "."
        line.write(f"{e}{d} = {mime}")
        printer(line.getvalue())
        total_lines += 1

    if verbose >= 1:
        printer(f"Total codecs: {total_lines}")

    return 0
