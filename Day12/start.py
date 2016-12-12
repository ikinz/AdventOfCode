currLine = 0
data = {}
lines = []

def copy(args):
	global data
	if not args[1] in data:
		data[args[1]] = 0
	try:
		data[args[1]] = int(args[0])
	except ValueError:
		data[args[1]] = data[args[0]]

def incr(args):
	global data
	if not args[0] in data:
		data[args[0]] = 0
	data[args[0]] += 1

def decr(args):
	global data
	if not args[0] in data:
		data[args[0]] = 0
	data[args[0]] -= 1

def jump(args):
	global currLine, data
	try:
		if int(args[0]) != 0:
			currLine += int(args[1]) - 1		# -1 to compensate +1 in the loop
	except ValueError:
		if not args[0] in data:
			data[args[0]] = 0
		if data[args[0]] != 0:
			currLine += int(args[1]) - 1		# -1 to compensate +1 in the loop

instr = {
	"cpy": copy,
	"inc": incr,
	"dec": decr,
	"jnz": jump
}

with open("input.txt", "r") as f:
	for line in f:
		lines.append(line.replace("\n", ""))

# Part 1
# -----------------------------
while currLine < len(lines):
	split = lines[currLine].split(" ")
	instr[split[0]](split[1:])
	currLine += 1

with open("output_part1.txt", "w") as o:
	o.write(str(data["a"]))


# Part 2
# -----------------------------
currLine = 0
data = {"c": 1}

while currLine < len(lines):
	split = lines[currLine].split(" ")
	instr[split[0]](split[1:])
	currLine += 1

with open("output_part2.txt", "w") as o:
	o.write(str(data["a"]))