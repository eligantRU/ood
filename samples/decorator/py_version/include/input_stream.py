from abc import abstractmethod


class IInputStream:
    @abstractmethod
    def is_eof(self):
        pass

    @abstractmethod
    def read_byte(self):
        pass


class FileInputStream(IInputStream):
    _file_name = None
    _file = None

    def __init__(self, file_name):
        self._file_name = file_name

    def is_eof(self):
        pos = self._file.tell()
        byte = self._file.read(1)
        self._file.seek(pos)
        return not len(byte)

    def read_byte(self):
        return self._file.read(1)

    def __enter__(self):
        self._file = open(self._file_name, "rb")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()


class MemoryInputStream(IInputStream):
    _data = None
    _caret_pos = None

    def __init__(self, data):
        self._data = data
        self._caret_pos = 0

    def is_eof(self):
        return self._caret_pos is len(self._data)

    def read_byte(self):
        byte = self._data[self._caret_pos]
        self._caret_pos += 1
        return bytes(bytes([byte]))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


__all__ = [name.__name__ for name in [IInputStream, FileInputStream, MemoryInputStream]]
