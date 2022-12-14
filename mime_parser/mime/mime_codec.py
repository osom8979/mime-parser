# -*- coding: utf-8 -*-

from typing import Any, Callable, Optional, Union

from mime_parser.mime.mime_type import MimeType

MimeEncoder = Callable[[Any], bytes]
MimeDecoder = Callable[[bytes], Any]


class MimeCodec:
    def __init__(
        self,
        mime: Union[str, MimeType],
        encoder: Optional[MimeEncoder] = None,
        decoder: Optional[MimeDecoder] = None,
    ):
        if isinstance(mime, str):
            self.mime = MimeType.parse(mime)
        elif isinstance(mime, MimeType):
            self.mime = mime
        else:
            raise ValueError(f"Invalid `mime` type: {type(mime).__name__}")
        self.encoder = encoder
        self.decoder = decoder

    def __repr__(self) -> str:
        mime = self.mime.mime
        encoder = self.has_encoder()
        decoder = self.has_decoder()
        return f"MimeCodec(mime={mime},encoder={encoder},decoder={decoder})"

    def __str__(self) -> str:
        return self.mime.mime

    def has_encoder(self) -> bool:
        return self.encoder is not None

    def has_decoder(self) -> bool:
        return self.decoder is not None

    def set_encoder(self, encoder: MimeEncoder) -> None:
        self.encoder = encoder

    def set_decoder(self, decoder: MimeDecoder) -> None:
        self.decoder = decoder

    def remove_encoder(self) -> None:
        self.encoder = None

    def remove_decoder(self) -> None:
        self.decoder = None

    def encode(self, data: Any) -> bytes:
        if self.encoder is None:
            raise NotImplementedError(f"Not implemented {str(self.mime)} encoder")
        return self.encoder(data)

    def decode(self, data: bytes) -> Any:
        if self.decoder is None:
            raise NotImplementedError(f"Not implemented {str(self.mime)} decoder")
        return self.decoder(data)
