def getdata(filename, listname):
	with open(filename,'r') as infile:
		for value in infile:
			listname.append(int(value))


def main():
	data=[]

	getdata("/Users/sh/Documents/AoC_2020/day01/day01_input.txt", data)

		
	

if __name__ == '__main__':
	main()