from include.compressed_stream import *
from include.encrypted_stream import *
from include.output_stream import *
from include.input_stream import *
from sys import argv


def main():
    res2 = []
    with MemoryInputStream(bytes(bytes([1]) + b"A" + bytes([2]) + b"B" + bytes([1]) + b"C")) as input_stream,\
            MemoryOutputStream(res2) as output_stream:
        input_stream = CompressedMemoryInputStream(input_stream)
        res = []
        while not input_stream.is_eof():
            res.append(input_stream.read_byte())
        print("".join(map(chr, res)))
        output_stream = CompressedMemoryOutputStream(output_stream)
        for byte in bytearray(res):
            output_stream.write_byte(byte)
        output_stream.flush()
        print(res2)
    print()

    with FileInputStream("1.txt") as input_stream, FileOutputStream("2.txt") as output_stream:
        input_stream = CompressedFileInputStream(input_stream)
        output_stream = CompressedFileOutputStream(output_stream)
        res = []
        while not input_stream.is_eof():
            byte = input_stream.read_byte()
            res.append(byte)
        print(res)

        for byte in res:
            output_stream.write_byte(byte)
        output_stream.flush()
    print()

    # res2 = []
    # with MemoryInputStream(bytes(bytes([190, 189, 189, 188]))) as input_stream,\
    #         MemoryOutputStream(res2) as output_stream:
    #     input_stream = EncryptedMemoryInputStream(input_stream, key=0xFF)
    #     output_stream = EncryptedMemoryOutputStream(output_stream, key=0xFF)
    #     res = []
    #     while not input_stream.is_eof():
    #          res.append(input_stream.read_byte())
    #     print("".join(map(chr, res)))
    #     for byte in bytearray(res):
    #         output_stream.write_byte(byte)
    #     output_stream.flush()
    #     print(res2)


if __name__ == "__main__":
    # main()

    # python __main__.py --decompress 1.txt 2.txt   ->    python __main__.py --encrypt 30 --decrypt 30  2.txt 3.txt
    #

    with FileInputStream(argv[-2]) as inp, FileOutputStream(argv[-1]) as out:
        argv = argv[1:-2]

        i = 0
        while i < len(argv):
            if argv[i] == "--encrypt":
                i += 1
                out = EncryptedFileOutputStream(out, int(argv[i]))
            elif argv[i] == "--compress":
                out = CompressedFileOutputStream(out)
            elif argv[i] == "--decrypt":
                i += 1
                inp = EncryptedFileInputStream(inp, int(argv[i]))
            elif argv[i] == "--decompress":
                inp = CompressedFileInputStream(inp)
            else:
                print("Unknown argument: ", argv[i])
            i += 1

        while not inp.is_eof():
            bla = inp.read_byte()
            print(bla)
            out.write_byte(bla)
        out.flush()
