import time
import zlib
import struct

def write32u(value):
    return struct.pack('<L', value)

def write_gzip_header():
    header = ''
    header += '\037\213'                  # magic header (0x1f, 0x8b)
    header += '\010'                      # compression method (deflate)
    header += '\000'                      # flags (not set)
    header += write32u(long(time.time())) # file modification time
    header += '\002'                      # extra flags (maximum compression)
    header += '\377'                      # os type (unknown)
    return header

def write_gzip_footer(crc, size):
    footer = ''
    footer += write32u(crc)
    footer += write32u(size & 0xffffffffL)
    return footer

def compress(input, compresslevel=6):
    crc  = zlib.crc32('') & 0xffffffffL
    size = 0
    yield write_gzip_header()
    compress = zlib.compressobj(compresslevel, zlib.DEFLATED, -zlib.MAX_WBITS, zlib.DEF_MEM_LEVEL, 0)
    for data in input:
        crc = zlib.crc32(data, crc) & 0xffffffffL
        size += len(data)
        compressed = compress.compress(data)
        if len(compressed) > 0: yield compressed
    yield compress.flush() + write_gzip_footer(crc, size)