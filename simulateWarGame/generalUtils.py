#TODO: merge the next 2 functions (args, kargs)
def readPositiveInteger(what, min, max):
	while True:
		readInteger = readPositiveInt(what)
		if readInteger >= min and readInteger <= max:
			break
	return readInteger

def readPositiveInt(what):
	while True:
		try:
			readInteger = int(input("Please provide the numbers of {} :".format(what)))
			if readInteger > 0:
				break
		except TypeError:
			print("Please enter an integer")
	return readInteger