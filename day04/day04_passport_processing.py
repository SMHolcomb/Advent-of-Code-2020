# --- Day 4: Passport Processing ---
# You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. 
# While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't 
# actually valid documentation for travel in most of the world.

# It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport 
# scanners, and the delay could upset your travel itinerary.

# Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.

# The automatic passport scanners are slow because they're having trouble detecting which passports have all required 
# fields. The expected fields are as follows:

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
# Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value 
# pairs separated by spaces or newlines. Passports are separated by blank lines.

# Here is an example batch file containing four passports:

# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm

# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929

# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm

# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in
# The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the Height field).

# The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, 
# not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat 
# this "passport" as valid.

# The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.

# According to the above rules, your improved system would report 2 valid passports.

# Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
# --- Part Two ---
# The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!

# You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
# Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:


import re

        
def getdata(filename,listname):
		with open(filename, 'r') as f:
			return f.read().split('\n\n')
	
def isValid(string):
	mandatory = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	if all([field in string for field in mandatory]):
		return True
	else:
		return False

def isValid_part2(passport,clean_passports):
	passport = clean_passports[passport]
	eye_colors = ['amb','blu','brn','gry','grn','hzl','oth']
	if(1920<=int(passport['byr'])<=2002 
	and 2010<=int(passport['iyr'])<=2020
	and 2020<=int(passport['eyr'])<=2030 
	and ( ( 'cm' in passport['hgt'] and 150 <= int(passport['hgt'].replace('cm',''))  <=193)  or ( 'in' in passport['hgt'] and 59 <= int(passport['hgt'].replace('in','')) <= 76  ) )
	and passport['ecl'] in eye_colors
	and re.match(r"^#[a-f0-9]{6}",passport['hcl'])
	and len(passport['pid']) == 9
	and re.match(r"^[0-9]{9}", passport['pid'])):
	  	return True
	else:
		return False
	

def main():

	# -- Part I --
	data = []
	valid_passports = []
	data = getdata("/Users/sh/Documents/AoC_2020/day04/day04_input.txt",data)

	for passport in data:
		if(isValid(passport)):
			valid_passports.append(passport)
	print("Part I - Valid passports:", len(valid_passports))

	# *** 254 *** 


	# -- Part II --

	# only need to check valid passports for additional requirements
	clean_passports = {}

	for i in range(0,len(valid_passports)):
		clean_passports[i]={}
		for item in re.split(' |\n',valid_passports[i]):
			
			item = item.split(':')
			if(item!=''):
				if(len(item)<2):
					continue
				else:
					clean_passports[i][item[0]] = item[1]
	
	count=0
	for num,passport in enumerate(clean_passports):
		if isValid_part2(passport,clean_passports):
			count+=1

	print("Part II - Valid passports:",count)

if __name__ == '__main__':
	main()