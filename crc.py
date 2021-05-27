#!/usr/bin/python

import binascii

info = '''A program which can be run to return the CRC32 value of a specified
file (in hex and dec).
Run with Python 3 installed and follow the instructions.
'''

todo = '''Have it loop around unless a certain filename is entered (or blank).
'''


def load_binary_data_from_file(filepath):
    '''rb = Read in Binary format.
    IOError exception may be raised if file cannot be read.
    '''
    with open(filepath, 'rb') as f:
        return f.read()


def get_crc32(in_data):
    '''Must be in binary form such as the string: b"hello world".
    '''
    return binascii.crc32(in_data) & 0xffffffff


def get_crc32_of_file(filepath):
    return get_crc32(load_binary_data_from_file(filepath))


def format_crc32(crc_value):
    '''Hex value zero padded to 8 digits long.
    '''
    # 'hex=%08X dec=%d' % (crc_value, crc_value)
    return 'hex={0:08X} dec={0:d}'.format(crc_value)


def get_formatted_crc32(in_data):
    return format_crc32(get_crc32(in_data))


def get_formatted_crc32_of_file(filepath):
    return format_crc32(get_crc32_of_file(filepath))


if __name__ == "__main__":
    print('CRC32 Calculator')

    while True:
        filepath = input('\nEnter filepath (blank to exit): ').strip()
        if not filepath:
            break
        print()

        try:
            crc_formatted = get_formatted_crc32_of_file(filepath)
        except IOError:
            print('File does not exist: %s' % (filepath))
        else:
            print('CRC of "%s":\n%s' % (filepath, crc_formatted))
