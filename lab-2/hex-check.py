
if __name__=='__main__':
	numTotal = 0
	numCorrect = 0
	with open('sub.tex', 'r') as f:
		lines = f.readlines()
		for line in lines:
			numTotal += 1
			nums = line.split()
			if len(nums) == 3:
				if int(nums[0], 10) == int(nums[1], 2) and  int(nums[1], 2) == int(nums[2], 16):
					numCorrect += 1
			if numTotal == 5:
				break

	print numCorrect, 'correct (out of 5)'
