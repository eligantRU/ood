from include.output_stream import *
from include.input_stream import *


class EncryptedMemoryInputStream(IInputStream):
    _strm = None
    _key = None

    def __init__(self, strm, key):
        self._strm = strm
        self._key = key

    def read_byte(self):
        return bytes([self._strm.read_byte()[0] ^ self._key])

    def is_eof(self):
        return self._strm.is_eof()


class EncryptedMemoryOutputStream(IOutputStream):
    _strm = None
    _key = None

    def __init__(self, strm, key):
        self._strm = strm
        self._key = key

    def write_byte(self, byte):
        self._strm.write_byte(byte ^ self._key)


class EncryptedFileInputStream(IInputStream):
    _strm = None
    _key = None

    def __init__(self, strm, key):
        self._strm = strm
        self._key = key

    def read_byte(self):
        return bytes([self._strm.read_byte()[0] ^ self._key])

    def is_eof(self):
        return self._strm.is_eof()


class EncryptedFileOutputStream(IOutputStream):
    _strm = None
    _key = None

    def __init__(self, strm, key):
        self._strm = strm
        self._key = key

    def write_byte(self, byte):
        self._strm.write_byte(bytes([byte[0] ^ self._key]))


__all__ = [name.__name__ for name in [EncryptedMemoryInputStream, EncryptedMemoryOutputStream, EncryptedFileInputStream, EncryptedFileOutputStream]]
