'''
  This scipt converts a hex file to an array to be copied and saved into a program.
  Used for data dump debugging in microcontrollers and saving the data from memory
  into a hex file.

  author: Sijin Woo
'''
fileName = 'leftSpeedDump'		# Change to match hex file name
length = 8						# Change to match size of each element 
								# 4 = 16 bytes, 8 = 32 bytes

data = []

def main():
	try:
		f = open(fileName, 'r')
		for line in f:
			print(line)
			charCnt = int(line[1:3], 16)
			print(charCnt)
			for i in range(0, int(charCnt / (length / 2))):
				value = '0x' + str(line[9 + i * length:9 + i * length + length]);
				data.append(int(value, 16))
				print(value)
		printList(data)
		#data = makeMonolithic(data)
		f.close()
	except:
		print('failed')

def makeMonolithic(listArg):
	prevVal = listArg[0]
	for i in range(1, len(listArg) - 1):
		if prevVal > listArg[i]:
			listArg[i] = (listArg[i + 1] + prevVal) / 2
		prevVal = listArg[i]
	return listArg

def printList(listArg):
	for element in listArg:
		print(element)

if __name__ == '__main__':
	main()
