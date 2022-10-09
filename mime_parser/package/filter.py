# -*- coding: utf-8 -*-

from pkgutil import iter_modules
from typing import List, Optional, Sequence

from mime_parser.regex.access_filter import UnionPattern, access_filter


def startswith_module_names(prefix: str) -> List[str]:
    return [m.name for m in iter_modules() if m.name.startswith(prefix)]


def filter_module_names(
    prefix: str,
    denies: Optional[Sequence[UnionPattern]] = None,
    allows: Optional[Sequence[UnionPattern]] = None,
) -> List[str]:
    return access_filter(
        names=startswith_module_names(prefix),
        denies=denies,
        allows=allows,
    )
