# -*- coding: utf-8 -*-

from typing import Final, List, Optional, Tuple

TYPE_SEPARATOR: Final[str] = "/"
PARAMETER_SEPARATOR: Final[str] = ";"
ANY_WILDCARD: Final[str] = "*"


class MimeType:
    """
    A media type (formerly known as MIME type) is a two-part identifier
    for file formats and format contents transmitted on the Internet.

    See also:
    * https://en.wikipedia.org/wiki/Media_type
    * https://datatracker.ietf.org/doc/html/rfc2045#section-5.1
    * https://www.iana.org/assignments/media-types/media-types.xhtml
    """

    def __init__(
        self,
        family: str,
        subtype: str,
        parameter: Optional[str] = None,
        original: Optional[str] = None,
        name: Optional[str] = None,
        reference: Optional[str] = None,
    ):
        # The `type` of MIME is a Python reserved character.
        # Therefore, the name will be changed to `family`.
        self.family = family.strip().lower()

        # Does not parse `tree` and `suffix`.
        self.subtype = subtype.strip().lower()

        # Does not parse `attribute` and `value`.
        self.parameter = parameter

        # Full original text.
        self.original = original

        self.name = name
        self.reference = reference

    @property
    def mime(self) -> str:
        prefix = f"{self.family}{TYPE_SEPARATOR}{self.subtype}"
        if self.parameter:
            return f"{prefix}{PARAMETER_SEPARATOR}{self.parameter}"
        else:
            return prefix

    @property
    def parameter_tuple(self) -> Tuple[Optional[str], Optional[str]]:
        if not self.parameter:
            return None, None
        kv = self.parameter.split("=", 1)
        key = kv[0].strip()
        if len(kv) == 1:
            return key, None
        assert len(kv) == 2
        return key, kv[1].strip()

    def get_parameter_value(
        self,
        key: str,
        default_value: Optional[str] = None,
        lower_key=True,
    ) -> Optional[str]:
        pkey, pval = self.parameter_tuple
        if pkey is None or pval is None:
            return default_value
        pkey = pkey.lower() if lower_key else pkey
        if pkey != key:
            return default_value
        return pval

    @property
    def charset(self) -> Optional[str]:
        return self.get_parameter_value("charset", lower_key=True)

    @property
    def q(self) -> Optional[float]:
        val = self.get_parameter_value("q", lower_key=True)
        if val is None:
            return None
        try:
            return float(val)
        except ValueError:
            return None

    @classmethod
    def parse(
        cls,
        text: str,
        name: Optional[str] = None,
        reference: Optional[str] = None,
    ) -> "MimeType":
        types_and_param = text.split(PARAMETER_SEPARATOR, 1)
        assert 1 <= len(types_and_param) <= 2

        parameter: Optional[str] = None
        if len(types_and_param) == 2:
            parameter = types_and_param[1].strip()

        types = types_and_param[0].strip().split(TYPE_SEPARATOR, 1)
        assert 1 <= len(types) <= 2

        family = types[0]
        if len(types) == 1:
            if family == ANY_WILDCARD:
                subtype = ANY_WILDCARD
            else:
                subtype = str()
        else:
            assert len(types) == 2
            subtype = types[1]

        return cls(family, subtype, parameter, text, name, reference)

    def __str__(self) -> str:
        return self.mime

    def __repr__(self) -> str:
        return self.mime

    def accept(self, mime: "MimeType") -> bool:
        if self.family == mime.family:
            pass
        elif mime.family == ANY_WILDCARD:
            pass
        elif self.family == ANY_WILDCARD:
            pass
        else:
            assert self.family != mime.family
            return False

        if self.subtype == mime.subtype:
            return True
        elif mime.subtype == ANY_WILDCARD:
            return True
        elif self.subtype == ANY_WILDCARD:
            return True
        else:
            assert self.subtype != mime.subtype
            return False

    def accepts(self, mimes: List["MimeType"]) -> bool:
        for accept in mimes:
            if self.accept(accept):
                return True
        return False


def parse_mime(
    text: str,
    name: Optional[str] = None,
    reference: Optional[str] = None,
) -> MimeType:
    return MimeType.parse(text, name, reference)
