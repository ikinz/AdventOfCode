resPt1 = 0

with open("input.txt", "r") as f:
	for line in f:
		insideBrackets = False
		for x in range(len(line)-4):
			sub = line[x:x+4]
			if "[" in sub:
				insideBrackets = True
			elif insideBrackets:
				if line[x] == "]":
					insideBrackets = False
			else:
				if sub[0] == sub[1] and "".join(sub[:2]) == "".join(reversed(sub[2:])):
					resPt1 += 1

with open("output_part1.txt", "w") as o:
	o.write(str(resPt1))