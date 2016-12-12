resPt1 = 0
resPt2 = 0

# Part 1
# ----------------------------------
with open("input.txt", "r") as f:
	for line in f:
		split = [int(x) for x in line.split()]
		split.sort()
		if split[0] + split[1] > split[2]:
			resPt1 += 1

with open("output_part1.txt", "w") as o:
	o.write(str(resPt1))

# Part 2
# ----------------------------------
def checkTriangle(arr):
	arr.sort()
	return arr[0] + arr[1] > arr[2]

arr = []
with open("input.txt", "r") as f:
	for line in f:
		arr.append([int(x) for x in line.split()])

x = 0
for i in range(len(arr[0])):
	vals = []
	for j in range(len(arr)):
		vals.append(arr[j][i])
		x += 1
		if x >= 3:
			if checkTriangle(vals):
				resPt2 += 1
			vals = []
			x = 0

with open("output_part2.txt", "w") as o:
	o.write(str(resPt2))