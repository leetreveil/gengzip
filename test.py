import unittest
import StringIO
import gzip
from gengzip import compress

def decompress_data(fileobj):
    gfile = gzip.GzipFile(fileobj=fileobj, mode='rb')
    result = gfile.read()
    gfile.close()
    return result

class tests(unittest.TestCase):

    def test_should_be_able_to_compress_a_list_of_data(self):
        input = ['123', '45']

        sio = StringIO.StringIO()
        for compressed in compress(input):
            sio.write(compressed)
        sio.seek(0)

        result = decompress_data(sio)
        self.assertEqual(result, ''.join(input))

    def test_should_be_able_to_compress_data_coming_from_a_generator(self):
        input = '12345'
        def gen():
            yield input

        sio = StringIO.StringIO()
        for compressed in compress(gen()):
            sio.write(compressed)
        sio.seek(0)

        result = decompress_data(sio)
        self.assertEqual(result, input)

    def test_should_be_able_to_compress_0_bytes_of_data(self):
        input = ['']

        sio = StringIO.StringIO()
        for compressed in compress(input):
            sio.write(compressed)
        sio.seek(0)

        result = decompress_data(sio)
        self.assertEqual(result, '')

    def test_should_be_able_to_set_the_compression_level(self):
        list(compress('', compresslevel=1))

if __name__ == '__main__':
    unittest.main()