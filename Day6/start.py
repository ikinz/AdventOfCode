arr = []
resPt1 = ""
resPt2 = ""

with open("input.txt", "r") as f:
	firstRun = True
	for line in f:
		i = 0
		while i < len(line):
			if firstRun:
				arr.append({})
			if line[i] in arr[i]:
				arr[i][line[i]] += 1
			else:
				arr[i][line[i]] = 1
			i += 1
		firstRun = False

# Part 1
# -------------------------------------
for d in arr:
	bestKey = ""
	bestValue = 0
	for key in d:
		if d[key] > bestValue:
			bestKey = key
			bestValue = d[key]
	resPt1 += bestKey

with open("output_part1.txt", "w") as o:
	o.write(resPt1)

# Part 2
# -------------------------------------
for d in arr:
	bestKey = ""
	bestValue = 999999
	for key in d:
		if d[key] < bestValue:
			bestKey = key
			bestValue = d[key]
	resPt2 += bestKey

with open("output_part2.txt", "w") as o:
	o.write(resPt2)