# -*- coding: utf-8 -*-

from typing import Any, Callable, Dict, Union

from mime_parser.codec.mime_codec import MimeCodec

MimeEncoder = Callable[[Any], bytes]
MimeDecoder = Callable[[bytes], Any]


class MimeCodecRegister(Dict[str, MimeCodec]):
    def register(self, codec: MimeCodec) -> None:
        self.__setitem__(str(codec.mime), codec)

    def unregister(self, mime: Union[str, MimeCodec]) -> None:
        if isinstance(mime, str):
            self.__delitem__(mime)
        elif isinstance(mime, MimeCodec):
            self.__delitem__(str(mime.mime))
        else:
            raise TypeError(f"Unsupported mime type: {type(mime).__name__}")

    def has_encoder(self, mime: str) -> bool:
        if not self.__contains__(mime):
            return False
        return self.__getitem__(mime).has_encoder()

    def has_decoder(self, mime: str) -> bool:
        if not self.__contains__(mime):
            return False
        return self.__getitem__(mime).has_decoder()

    def set_encoder(self, mime: str, encoder: MimeEncoder) -> None:
        if self.__contains__(mime):
            self.__getitem__(mime).set_encoder(encoder)
        else:
            self.__setitem__(mime, MimeCodec(mime, encoder=encoder))

    def set_decoder(self, mime: str, decoder: MimeDecoder) -> None:
        if self.__contains__(mime):
            self.__getitem__(mime).set_decoder(decoder)
        else:
            self.__setitem__(mime, MimeCodec(mime, decoder=decoder))

    def encode(self, mime: str, data: Any) -> bytes:
        return self.__getitem__(mime).encode(data)

    def decode(self, mime: str, data: bytes) -> Any:
        return self.__getitem__(mime).decode(data)
