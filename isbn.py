#!/usr/bin/python

import string

ten = 'X'

ISBN_DET = {}
ISBN_DET[10] = {'mul': list(range(10, 0, -1)), 'mod': 11}
ISBN_DET[13] = {'mul': [1, 3], 'mod': 10}


def multiply(x, y):
    if x in ten:
        return 10*int(y)
    else:
        return int(x)*int(y)


def expand_mul(seq, leng):
    outlist = seq * ((leng // len(seq)) + 1)

    # reduce the amount by one until the amount is exactly right otherwise
    # the map function this is used in breaks
    while leng < len(outlist):
        outlist = outlist[:-1]

    return outlist


def check(isbn, give_checksum=False, case_sensitive=False):
    '''Autodetection of type of ISBN system being used (via length).
    Default to checking a complete ISBN.
    '''
    isbn = isbn.strip()

    if not case_sensitive:
        isbn = isbn.upper()

    if give_checksum:
        isbn = ''.join([item for item in isbn if item in string.digits])
    else:
        isbn = ''.join([item for item in isbn if item in string.digits + ten])

        if ten in isbn[:-1]:
            raise ValueError('X may only be at the end')

    length = len(isbn)
    if give_checksum:
        length += 1

    # if the particular length of ISBN is defined above in ISBN_DET then
    # process it, otherwise raise exception
    if length not in ISBN_DET:
        raise ValueError('Invalid length')
    else:
        # cause the mul to be continuously repeated until it is >= to the
        # isbn in terms of the length
        mul = expand_mul(ISBN_DET[length]['mul'], len(isbn))
        mod = ISBN_DET[length]['mod']

        total_list = map(multiply, isbn, mul)
        total = 0
        for n in total_list:
            total += n

        if give_checksum:
            checksum = mod - (total % mod)
            if checksum == 10:
                return ten[0]
            else:
                return checksum
        else:
            return total % mod == 0


def command_line(args):
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
            elif arg in ('-s', '--sum'):
                type = True
            elif arg in ('-c', '--check'):
                type = False
            else:
                result_display(arg, type)
    else:
        print('ISBN number checker\n')
        while True:
            isbn = input(
                'Enter an ISBN Number (leave blank to quit): ').strip()
            if not isbn:
                break

            while (True):
                checksum_str = input(
                    'Type 0 (default) for Check' +
                    'or 1 for Checksum generation: ').strip()
                if checksum_str:
                    try:
                        give_checksum = int(checksum_str)
                    except ValueError:
                        continue
                    else:
                        break
                else:
                    give_checksum = False
                    break

            result_display(isbn, give_checksum)


def result_display(isbn, give_checksum=None):
    try:
        print(check(isbn, give_checksum))
    except ValueError as e:
        print(e)
    print()


if __name__ == '__main__':
    import sys
    command_line(sys.argv)
