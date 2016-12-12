pad  = [["1","4","7"],["2","5","8"],["3","6","9"]]
pad2 = [["-","-","5","-","-"],
		  ["-","2","6","A","-"],
		  ["1","3","7","B","D"],
		  ["-","4","8","C","-"],
		  ["-","-","9","-","-"]]
x = 1
y = 1
resPt1 = ""
resPt2 = ""

# RUDULRLLU U L RU RDDR R UDUR ULLLDRLRLUDDLUDUDDUDRRDUDULDUUULLRULLRLDDLDLDDRLRRRRUD
# 636323211 1 1 22 3699 9 6966

  # 1 2 3
  # 4 5 6
  # 7 8 9

def parseChar(ch):
	global x, y
	if ch.isalpha():
		if ch == "U" and y > 0:
			y -= 1
		elif ch == "D" and y < 2:
			y += 1
		elif ch == "L" and x > 0:
			x -= 1
		elif ch == "R" and x < 2:
			x += 1

# Part 1
with open("input.txt", "r") as f:
	for line in f:
		for c in line:
			parseChar(c)
		resPt1 += pad[x][y]

with open("output_part1.txt", "w") as o:
	o.write(resPt1)


# Part 2
def parseChar2(ch):
	global x, y
	if ch.isalpha():
		if ch == "U" and y > 0 and (not pad2[x][y-1] == "-"):
			y -= 1
		elif ch == "D" and y < 4 and (not pad2[x][y+1] == "-"):
			y += 1
		elif ch == "L" and x > 0 and (not pad2[x-1][y] == "-"):
			x -= 1
		elif ch == "R" and x < 4 and (not pad2[x+1][y] == "-"):
			x += 1

x = 0
y = 2
with open("input.txt", "r") as f:
	for line in f:
		for c in line:
			parseChar2(c)
		resPt2 += pad2[x][y]

with open("output_part2.txt", "w") as o:
	o.write(resPt2)