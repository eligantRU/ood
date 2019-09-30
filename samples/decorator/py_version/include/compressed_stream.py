from include.output_stream import *
from include.input_stream import *


class CompressedInputStream(IInputStream):
    _strm = None
    _buffer = None

    def __init__(self, strm):
        self._strm = strm
        self._buffer = 0, None

    def read_byte(self):
        size, byte = self._buffer
        if size is 0:
            size, byte = int.from_bytes(self._strm.read_byte(), byteorder="big"), self._strm.read_byte()
        self._buffer = size - 1, byte
        return self._buffer[1]

    def is_eof(self):
        if self._strm.is_eof() and self._buffer[0] is not 0:
            return False
        return self._strm.is_eof()


class CompressedOutputStream(IOutputStream):
    _strm = None
    _last = None
    _counter = None

    def __init__(self, strm):
        self._strm = strm
        self._counter = 0

    def write_byte(self, byte):
        if self._last is None:
            self._last = byte
            self._counter -= 1

        if byte == self._last:
            self._counter += 1
            if self._counter == 255:
                self._write_impl(255, self._last)
        else:
            self._write_impl(self._counter + 1, self._last)
            self._last = byte

    def flush(self):
        self._write_impl(self._counter + 1, self._last)

    def _write_impl(self, counter, last):
        self._strm.write_byte(bytes([counter]))
        self._strm.write_byte(last)
        self._counter = 0


__all__ = [name.__name__ for name in [CompressedInputStream, CompressedOutputStream]]
