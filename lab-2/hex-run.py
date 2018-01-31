import random

if __name__ == '__main__':
	with open('sub.tex', 'w') as f:
		for i in random.sample(range(0,16), 5):
			f.write(str(i) + '\n')