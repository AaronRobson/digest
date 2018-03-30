#!/usr/bin/python

import string

ten = 'X'

ISBN_DET = {}
ISBN_DET[10] = {'mul': list(range(10, 0, -1)), 'mod': 11} # "range(10,0,-1)" or "range(10,1)[::-1]" suffices for "range(1,10,-1)"
ISBN_DET[13] = {'mul': [1, 3], 'mod': 10}

def Multiply(x, y):
	if x in ten:
		return 10*int(y)
	else:
		return int(x)*int(y)

def ExpandMul(seq, leng):
	#while len(outlist) <= leng: outlist += list # <= means it goes 1 repetition too far ie too many mul list items for the input list items
	outlist = seq * ((leng // len(seq)) + 1)

	#reduce the amount by one until the amount is exactly right otherwise the map function this is used in breaks
	while leng < len(outlist):
		outlist = outlist[:-1]

	return outlist

def IsbnCheck(isbn, giveChecksum=False, caseSensitive=False):
	'''Autodetection of type of ISBN system being used (via length). Default to checking a complete ISBN.
	'''
	#print('isbncheck - isbn: %r, giveChecksum: %s, caseSensitive: %s.' % (isbn, bool(giveChecksum), bool(caseSensitive)))

	isbn = isbn.strip()

	if not caseSensitive:
		isbn = isbn.upper()

	if giveChecksum:
		isbn = ''.join([item for item in isbn if item in string.digits])
	else:
		isbn = ''.join([item for item in isbn if item in string.digits + ten])

		if ten in isbn[:-1]:
			raise ValueError('X may only be at the end')

		# remove any x's from all but the last character of isbn
		#isbn = ''.join([item for item in isbn[:-1] if item in string.digits] + [isbn[-1:]])

	length = len(isbn)
	if giveChecksum:
		length += 1

	if length not in ISBN_DET: # if the particular length of ISBN is defined above in ISBN_DET then process it, otherwise raise exception
		raise ValueError('Invalid length')
	else:
		mul = ExpandMul(ISBN_DET[length]['mul'], len(isbn)) # cause the mul to be continuously repeated until it is >= to the isbn in terms of the length
		mod = ISBN_DET[length]['mod']

		totalList = map(Multiply, isbn, mul)
		total = 0
		for n in totalList:
			total += n

		#print isbn
		#print 'length of isbn ' + str(len(isbn))
		#print 'length of mul ' + str(len(mul))

		if giveChecksum:
			checkSum = mod - (total % mod)
			if checkSum == 10:
				return ten[0]
			else:
				return checkSum
		else:
			return total % mod == 0

def CommandLine(args):
	args = args[1:] #strip off the script filename (in the 0 position)

	if len(args):
		type = False #to default to checking complete ISBNs if not specified otherwise
		for arg in args:
			if arg in ('-h', '--help'):
				print ('Help: This program checks ISBN numbers of 10 and 13 lengths and calculates check digits')
			elif arg in ('-t', '--test'):
				ResultDisplay('ISBN0-596-00281-5') #True
				ResultDisplay('ISBN0-596-00281-', True) #5

				ResultDisplay('978-0-306-40615-7') #True
				ResultDisplay('978-0-306-40615-', True) #7

				ResultDisplay('1903397-26-x') #True
				ResultDisplay('1903397-26-', True) #X

				ResultDisplay('0-313-20060-2') #True
				ResultDisplay('0-313-20060-', True) #2
			elif arg in ('-s', '--sum'):
				type = True
			elif arg in ('-c', '--check'):
				type = False
			else:
				ResultDisplay(arg, type)
	else:
		print ('ISBN number checker\n')
		while (True):
			isbn = input('Enter an ISBN Number (leave blank to quit): ').strip()
			if not isbn:
				break

			while (True):
				checkSumStr = input('Type 0 (default) for Check or 1 for Checksum generation: ').strip()
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
		print (IsbnCheck(isbn, giveCheckSum))
	except ValueError as e:
		print(e)
	print ('')

if __name__ == '__main__':
	import sys
	CommandLine(sys.argv)
