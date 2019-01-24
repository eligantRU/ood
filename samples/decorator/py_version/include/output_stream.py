from abc import abstractmethod


class IOutputStream:
    @abstractmethod
    def write_byte(self, byte):
        pass

    @abstractmethod
    def flush(self):
        pass


class FileOutputStream(IOutputStream):
    _file_name = None
    _file = None

    def __init__(self, file_name):
        self._file_name = file_name

    def write_byte(self, byte):
        self._file.write(byte)

    def flush(self):
        pass

    def __enter__(self):
        self._file = open(self._file_name, "wb")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()


class MemoryOutputStream:
    _data = None

    def __init__(self, data):
        self._data = data

    def write_byte(self, byte):
        self._data.append(byte)

    def flush(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


__all__ = [name.__name__ for name in [IOutputStream, FileOutputStream, MemoryOutputStream]]
