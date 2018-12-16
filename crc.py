#!/usr/bin/python

import binascii

info = '''A program which can be run to return the CRC32 value of a specified
file (in hex and dec).
Run with Python 3 installed and follow the instructions.
'''

todo = '''Have it loop around unless a certain filename is entered (or blank).
'''


def LoadBinaryDataFromFile(filepath):
    '''rb = Read in Binary format.
    IOError exception may be raised if file cannot be read.
    '''
    with open(filepath, 'rb') as f:
        return f.read()


def GetCRC32(inData):
    '''Must be in binary form such as the string: b"hello world".
    '''
    return binascii.crc32(inData) & 0xffffffff


def GetCRC32OfFile(filepath):
    return GetCRC32(LoadBinaryDataFromFile(filepath))


def FormatCRC32(crcValue):
    '''Hex value zero padded to 8 digits long.
    '''
    # 'hex=%08X dec=%d' % (crcValue, crcValue)
    return 'hex={0:08X} dec={0:d}'.format(crcValue)


def GetFormatedCRC32(inData):
    return FormatCRC32(GetCRC32(inData))


def GetFormatedCRC32OfFile(filepath):
    return FormatCRC32(GetCRC32OfFile(filepath))


if __name__ == "__main__":
    print('CRC32 Calculator')

    while True:
        filepath = input('\nEnter filepath (blank to exit): ').strip()
        if not filepath:
            break
        print()

        try:
            crcFormatted = GetFormatedCRC32OfFile(filepath)
        except IOError:
            print('File does not exist: %s' % (filepath))
        else:
            print('CRC of "%s":\n%s' % (filepath, crcFormatted))
