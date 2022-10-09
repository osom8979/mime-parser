# -*- coding: utf-8 -*-

from gzip import compress, decompress

from mime_parser.favorite import APPLICATION_GZIP
from mime_parser.mime.mime_codec import MimeCodec

codec = MimeCodec(mime=APPLICATION_GZIP, encoder=compress, decoder=decompress)
