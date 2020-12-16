# --- Day 5: Binary Boarding ---
# You board your plane only to discover a new problem: you dropped your boarding pass! 
# You aren't sure which seat is yours, and all of the flight attendants are busy with 
# the flood of people that suddenly made it through passport control.

# You write a quick program to use your phone's camera to scan all of the nearby boarding 
# passes (your puzzle input); perhaps you can find your seat through process of elimination.

# Instead of zones or groups, this airline uses binary space partitioning to seat people. A 
# seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", 
# and R means "right".

# The first 7 characters will either be F or B; these specify exactly one of the 128 rows on 
# the plane (numbered 0 through 127). Each letter tells you which half of a region the given 
# seat is in. Start with the whole list of rows; the first letter indicates whether the seat 
# is in the front (0 through 63) or the back (64 through 127). The next letter indicates which 
# half of that region the seat is in, and so on until you're left with exactly one row.

# The last three characters will be either L or R; these specify exactly one of the 8 c
# olumns of seats on the plane (numbered 0 through 7). The same process as above proceeds 
# again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

# For example, consider just the last 3 characters of FBFBBFFRLR:

# Start by considering the whole range, columns 0 through 7.
# R means to take the upper half, keeping columns 4 through 7.
# L means to take the lower half, keeping columns 4 through 5.
# The final R keeps the upper of the two, column 5.
# So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.


# Every seat also has a unique seat ID: multiply the row by 8, then add the column.


# --- Part Two ---
# Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

# It's a completely full flight, so your seat should be the only missing boarding pass in your 
# list. However, there's a catch: some of the seats at the very front and back of the plane 
# don't exist on this aircraft, so they'll be missing from your list as well.

# Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 
# from yours will be in your list.

# What is the ID of your seat?



import re

        
def getdata(filename,listname):
    with open(filename, 'r') as infile:
        for line in infile:
            listname.append(line.rstrip('\n'))
			
        #print(listname)

	

def main():
    test=[]
    getdata("/Users/sh/Documents/AoC_2020/day05/day05_input.txt",test)
    seats=[]
    #test = ('FBFBBFFRLR' ,'BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL')

    for j in range(0, len(test)):

       
        min_ = 0
        max_ = 127
       
        for i in range(0,7):  #0-7
            if test[j][i] == 'F':
                max_ = min_ + ((max_ - min_ + 1)/2)-1
                #print(i,":",min_,max_) 
            if test[j][i] =='B':
                min_ = min_ + ((max_ - min_ + 1) / 2)
                #print(i,":",min_,max_)
        rownum=min_
        #print("rownum:", rownum)


        # now handle the last 3
        min_ = 0
        max_ = 7
        column = 0
        for i in range(7, 9):  # 8-9
            #print(test[j][i])
            
            if test[j][i] == 'R':
                min_=min_+((max_-min_+1)/2)
                #print(i,":",min_,max_)
            if test[j][i]== 'L':
                max_ = min_ + ((max_-min_+1) / 2)-1
                #print(i,":",min_,max)
        

            if test[j][9]=='R':
                column = max_
            elif test[j][9]=='L':
                column = min_

           

        seatID = int(rownum * 8 + column)

        #print("rownum:", rownum, "  column:", column, "seatid:", seatID) 
        seats.append(seatID)
    print("PART I:", max(seats))
    # 918

    ## PART II
    seats = sorted(seats)
    # https://stackoverflow.com/questions/20718315/how-to-find-a-missing-number-from-a-list
    print("Part II:", sum(range(seats[0],seats[-1]+1)) - sum(seats))
    # 717


if __name__ == '__main__':
	main()