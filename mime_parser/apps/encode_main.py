# -*- coding: utf-8 -*-

from argparse import Namespace
from sys import stdin, stdout

from mime_parser.global_register import encode


def main(args: Namespace) -> int:
    assert args is not None

    mime = args.mime
    assert isinstance(mime, str)

    data = bytes()
    try:
        data = stdin.buffer.read()
    except EOFError:
        stdin.buffer.flush()

    if data:
        stdout.buffer.write(encode(mime, data))
        return 0
    else:
        return 1
