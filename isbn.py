#!/usr/bin/python

import string

ten = 'X'

ISBN_DET = {}
ISBN_DET[10] = {'mul': list(range(10, 0, -1)), 'mod': 11}
ISBN_DET[13] = {'mul': [1, 3], 'mod': 10}


def Multiply(x, y):
    if x in ten:
        return 10*int(y)
    else:
        return int(x)*int(y)


def ExpandMul(seq, leng):
    outlist = seq * ((leng // len(seq)) + 1)

    # reduce the amount by one until the amount is exactly right otherwise
    # the map function this is used in breaks
    while leng < len(outlist):
        outlist = outlist[:-1]

    return outlist


def check(isbn, giveChecksum=False, caseSensitive=False):
    '''Autodetection of type of ISBN system being used (via length).
    Default to checking a complete ISBN.
    '''
    isbn = isbn.strip()

    if not caseSensitive:
        isbn = isbn.upper()

    if giveChecksum:
        isbn = ''.join([item for item in isbn if item in string.digits])
    else:
        isbn = ''.join([item for item in isbn if item in string.digits + ten])

        if ten in isbn[:-1]:
            raise ValueError('X may only be at the end')

    length = len(isbn)
    if giveChecksum:
        length += 1

    # if the particular length of ISBN is defined above in ISBN_DET then
    # process it, otherwise raise exception
    if length not in ISBN_DET:
        raise ValueError('Invalid length')
    else:
        # cause the mul to be continuously repeated until it is >= to the
        # isbn in terms of the length
        mul = ExpandMul(ISBN_DET[length]['mul'], len(isbn))
        mod = ISBN_DET[length]['mod']

        totalList = map(Multiply, isbn, mul)
        total = 0
        for n in totalList:
            total += n

        if giveChecksum:
            checkSum = mod - (total % mod)
            if checkSum == 10:
                return ten[0]
            else:
                return checkSum
        else:
            return total % mod == 0


def CommandLine(args):
    # strip off the script filename (in the 0 position)
    args = args[1:]

    if len(args):
        # to default to checking complete ISBNs if not specified otherwise
        type = False
        for arg in args:
            if arg in ('-h', '--help'):
                print(
                    'Help: This program checks ISBN numbers of 10 and 13' +
                    'lengths and calculates check digits')
            elif arg in ('-t', '--test'):
                ResultDisplay('ISBN0-596-00281-5')  # True
                ResultDisplay('ISBN0-596-00281-', True)  # 5

                ResultDisplay('978-0-306-40615-7')  # True
                ResultDisplay('978-0-306-40615-', True)  # 7

                ResultDisplay('1903397-26-x')  # True
                ResultDisplay('1903397-26-', True)  # X

                ResultDisplay('0-313-20060-2')  # True
                ResultDisplay('0-313-20060-', True)  # 2
            elif arg in ('-s', '--sum'):
                type = True
            elif arg in ('-c', '--check'):
                type = False
            else:
                ResultDisplay(arg, type)
    else:
        print('ISBN number checker\n')
        while True:
            isbn = input(
                'Enter an ISBN Number (leave blank to quit): ').strip()
            if not isbn:
                break

            while (True):
                checkSumStr = input(
                    'Type 0 (default) for Check' +
                    'or 1 for Checksum generation: ').strip()
                if checkSumStr:
                    try:
                        giveCheckSum = int(checkSumStr)
                    except ValueError:
                        continue
                    else:
                        break
                else:
                    giveCheckSum = False
                    break

            ResultDisplay(isbn, giveCheckSum)


def ResultDisplay(isbn, giveCheckSum=None):
    try:
        print(check(isbn, giveCheckSum))
    except ValueError as e:
        print(e)
    print()


if __name__ == '__main__':
    import sys
    CommandLine(sys.argv)
