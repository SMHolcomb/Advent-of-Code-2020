# --- Day 3: Toboggan Trajectory ---

#  --- PART I ---

# With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's 
# certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will 
# take you near the fewest trees.

# Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of 
# the open squares (.) and trees (#) you can see. For example:

# ..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#
# These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome 
# stability, the same pattern repeats to the right many times:

# ..##.........##.........##.........##.........##.........##.......  --->
# #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
# .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
# ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
# .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
# ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
# .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
# .#........#.#........#.#........#.#........#.#........#.#........#
# #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
# #...##....##...##....##...##....##...##....##...##....##...##....#
# .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
# You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

# The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); 
# start by counting all the trees you would encounter for the slope right 3, down 1:

# From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position 
# that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

# The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

# ..##.........##.........##.........##.........##.........##.......  --->
# #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
# .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
# ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
# .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
# ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
# .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
# .#........#.#........X.#........#.#........#.#........#.#........#
# #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
# #...##....##...##....##...#X....##...##....##...##....##...##....#
# .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
# In this example, traversing the map using this slope would cause you to encounter 7 trees.

# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?


# --- Part Two ---
# Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

# Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left 
# corner and traverse the map all the way to the bottom:

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
# In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

# What do you get if you multiply together the number of trees encountered on each of the listed slopes?



import numpy as np 

def getdata(filename,listname):
	with open(filename,'r') as infile:
		for line in infile:
			line = np.repeat(line.rstrip('\n'),10000)  # we need to repeat cols at least 101 times to be sure we are wide enough
			line = ("".join(line))
			listname.append(line)
    # A = np.loadtxt(filename, dtype = None)


def main():
	data=[]
	getdata("/Users/sh/Documents/AoC_2020/day03/day03_input.txt",data)
	# data = ['..##.........##.........##.........##.........##.........##.......',
	# 		'#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..',
	# 		'.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.',
	# 		'..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#',
	# 		'.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.',
	# 		'..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....',
	# 		'.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#',
	# 		'.#........#.#........#.#........#.#........#.#........#.#........#',
	# 		'#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...',
	# 		'#...##....##...##....##...##....##...##....##...##....##...##....#',
	# 		'.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#']

	slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

	#  PART I 
	row = col = 0
	treecount = 0
	#print(len(data))
	while row <=len(data)-2:
		if(data[row+1][col+3]=='#'):
			treecount+=1
		col+=3
		row+=1
	print("PART I - treecount:",treecount)
	# *** 272 trees ***

	# PART II
	treecount_product = 1
	print("d",data[10][1])
	for i in range(0,len(slopes)):
		print("slopes",slopes[i][0],slopes[i][1])
		
		row = col = 0
		treecount = 0
		col_add=slopes[i][0]
		row_add=slopes[i][1]
		while row <=len(data)-(row_add+1):
			if(data[row+row_add][col+col_add]=='#'):
				treecount+=1
			col+=col_add
			row+=row_add
		print("treecount", treecount)
		treecount_product = treecount_product * treecount
	print("PART I - treecount_product:",treecount_product)
	#  3898725600  too low

if __name__ == '__main__':
	main()