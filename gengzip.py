import gzip
import time
import zlib
import struct
import unittest
import StringIO

def write32u(value):
    # The L format writes the bit pattern correctly whether signed
    # or unsigned.
    return struct.pack('<L', value)

def write_gzip_header():
    header = ''
    header += '\037\213'                  # magic header (0x1f, 0x8b)
    header += '\010'                      # compression method (deflate)
    header += '\000'                      # flags (not set)
    mtime = time.time()
    header += write32u(long(mtime))       # file modification time
    header += '\002'                      # extra flags (maximum compression)
    header += '\377'                      # os type (unknown)
    return header

def write_gzip_footer(crc, size):
    footer = ''
    footer += write32u(crc)
    footer += write32u(size & 0xffffffff)
    return footer

def compress(input):
    crc  = zlib.crc32('') & 0xffffffff
    size = 0

    yield write_gzip_header()

    # just copying what python's gzip module does here,
    # TODO: find out what the options do
    compress = zlib.compressobj(9, zlib.DEFLATED, -zlib.MAX_WBITS, zlib.DEF_MEM_LEVEL, 0)
    
    for data in input:
        crc = zlib.crc32(data, crc) & 0xffffffff
        size += len(data)
        yield compress.compress(data)

    yield compress.flush()
    yield write_gzip_footer(crc, size)


class tests(unittest.TestCase):

    def decompress_data(self, fileobj):
        gfile = gzip.GzipFile(fileobj=fileobj, mode='rb')
        result = gfile.read()
        gfile.close()
        return result

    def test_should_be_able_to_compress_a_list_of_data(self):
        input = ['123', '45']

        sio = StringIO.StringIO()
        for compressed in compress(input):
            sio.write(compressed)
        sio.seek(0)

        result = self.decompress_data(sio)
        self.assertEqual(result, ''.join(input))

    def test_should_be_able_to_compress_data_coming_from_a_generator(self):
        input = '12345'
        def gen():
            yield input

        sio = StringIO.StringIO()
        for compressed in compress(gen()):
            sio.write(compressed)
        sio.seek(0)

        result = self.decompress_data(sio)
        self.assertEqual(result, input)

    def test_should_be_able_to_compress_0_bytes_of_data(self):
        input = ['']

        sio = StringIO.StringIO()
        for compressed in compress(input):
            sio.write(compressed)
        sio.seek(0)

        result = self.decompress_data(sio)
        self.assertEqual(result, '')

if __name__ == '__main__':
    unittest.main()
