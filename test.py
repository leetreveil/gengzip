import unittest
import six
import gzip
from gengzip import compress

def decompress_data(fileobj):
    gfile = gzip.GzipFile(fileobj=fileobj, mode='rb')
    result = gfile.read()
    gfile.close()
    return result

class tests(unittest.TestCase):

    def test_should_be_able_to_compress_a_list_of_data(self):
        input = [b'123', b'45']

        sio = six.BytesIO()
        for compressed in compress(input):
            sio.write(compressed)
        sio.seek(0)

        result = decompress_data(sio)
        self.assertEqual(result, b''.join(input))

    def test_should_be_able_to_compress_data_coming_from_a_generator(self):
        input = b'12345'
        def gen():
            yield input

        sio = six.BytesIO()
        for compressed in compress(gen()):
            sio.write(compressed)
        sio.seek(0)

        result = decompress_data(sio)
        self.assertEqual(result, input)

    def test_should_be_able_to_compress_0_bytes_of_data(self):
        input = [b'']

        sio = six.BytesIO()
        for compressed in compress(input):
            sio.write(compressed)
        sio.seek(0)

        result = decompress_data(sio)
        self.assertEqual(result, b'')

    def test_should_be_able_to_set_the_compression_level(self):
        list(compress(b'', compresslevel=1))

if __name__ == '__main__':
    unittest.main()
