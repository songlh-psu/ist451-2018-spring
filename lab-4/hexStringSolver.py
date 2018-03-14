import sys
import md5


if __name__ == '__main__':
	sFileName = sys.argv[1]
	dictMD5 = {}

	for num in range(256):
		c = chr(num)
		m = md5.new()
		m.update(c)
		dictMD5[m.hexdigest()] = c

	with open(sFileName, 'r') as f:
		lines = f.readlines()

		sResult = ''
		for line in lines:
			sResult += dictMD5[line[:-1]]

		print sResult