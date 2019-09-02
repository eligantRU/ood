from include.compressed_stream import *
from include.encrypted_stream import *
from include.output_stream import *
from include.input_stream import *
from sys import argv


def test_memory_streams():
    with MemoryInputStream(bytes([0x01, 0x27, 0x02, 0x1F])) as input_stream, MemoryOutputStream() as output_stream:
        input_stream = CompressedInputStream(input_stream)
        while not input_stream.is_eof():
            output_stream.write_byte(input_stream.read_byte())
        output_stream.flush()
        assert(output_stream._data == bytes([0x27, 0x1F, 0x1F]))

    with MemoryInputStream(bytes([0x01, 0x27, 0x02, 0x1F])) as input_stream, MemoryOutputStream() as output_stream:
        input_stream = CompressedInputStream(input_stream)
        output_stream = CompressedOutputStream(output_stream)
        while not input_stream.is_eof():
            output_stream.write_byte(input_stream.read_byte())
        output_stream.flush()
        assert(output_stream._strm._data == bytes([0x01, 0x27, 0x02, 0x1F]))

    with MemoryInputStream(bytes([0x27, 0x1F, 0x1F, 0xFF])) as input_stream, MemoryOutputStream() as output_stream:
        input_stream = EncryptedInputStream(input_stream, 0xFF)
        while not input_stream.is_eof():
            output_stream.write_byte(input_stream.read_byte())
        output_stream.flush()
        assert(output_stream._data == bytes([0xD8, 0xE0, 0xE0, 0x00]))

    with MemoryInputStream(bytes([0x27, 0x1F, 0x1F, 0xFF])) as input_stream, MemoryOutputStream() as output_stream:
        input_stream = EncryptedInputStream(input_stream, 0x83)
        while not input_stream.is_eof():
            output_stream.write_byte(input_stream.read_byte())
        output_stream.flush()
        assert(output_stream._data == bytes([0xA4, 0x9C, 0x9C, 0x7C]))

    with MemoryInputStream(bytes([0x01, 0x27, 0x02, 0x1F])) as input_stream, MemoryOutputStream() as output_stream:
        input_stream = CompressedInputStream(input_stream)
        input_stream = EncryptedInputStream(input_stream, 0xFF)
        output_stream = CompressedOutputStream(output_stream)
        while not input_stream.is_eof():
            output_stream.write_byte(input_stream.read_byte())
        output_stream.flush()
        assert(output_stream._strm._data == bytes([0x01, 0xD8, 0x02, 0xE0]))


def main(argv):
    test_memory_streams()

    with FileInputStream(argv[-2]) as inp, FileOutputStream(argv[-1]) as out:
        argv = argv[1:-2]

        i = 0
        while i < len(argv):
            if argv[i] == "--encrypt":
                i += 1
                out = EncryptedOutputStream(out, int(argv[i]))
            elif argv[i] == "--compress":
                out = CompressedOutputStream(out)
            elif argv[i] == "--decrypt":
                i += 1
                inp = EncryptedInputStream(inp, int(argv[i]))
            elif argv[i] == "--decompress":
                inp = CompressedInputStream(inp)
            else:
                print("Unknown argument: ", argv[i])
            i += 1

        while not inp.is_eof():
            out.write_byte(inp.read_byte())
        out.flush()

    # python __main__.py --decompress 1.txt out.txt
    # python __main__.py --encrypt 255 --compress 4.txt out.txt -> python __main__.py --decrypt 255 --decompress out.txt out2.txt
    # python __main__.py --encrypt 144 --encrypt 255 --compress 4.txt out.txt -> python __main__.py --decrypt 144 --decrypt 255 --decompress out.txt out2.txt


if __name__ == "__main__":
    main(argv)
