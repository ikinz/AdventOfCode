import time

currLine = 0
data = {"a":7}
lines = []

def getData(var):
	global data
	if var in data:
		return data[var]
	else:
		try:
			return int(var)
		except ValueError:
			data[var] = 0
			return data[var]

def copy(args):
	global data
	if not args[1] in data:
		try:
			int(args[1])
			return
		except ValueError:
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

def mult(args):
	global data
	data[args[2]] = getData(args[0]) * getData(args[1])

def jump(args):
	global currLine

	if getData(args[0]) != 0:
		currLine += getData(args[1]) - 1

def togl(args):
	global currLine, data, lines
	editLine = 0
	newLine = ""
	try:
		editLine = currLine + int(args[0])
	except ValueError:
		editLine = currLine + data[args[0]]

	if editLine >= 0 and editLine < len(lines):
		split = lines[editLine].split()
		if len(split[1:]) == 1:
			if split[0] == "inc":
				split[0] = "dec"
			else:
				split[0] = "inc"
		elif len(split[1:]) == 2:
			if split[0] == "jnz":
				split[0] = "cpy"
			else:
				split[0] = "jnz"
		newLine = " ".join(split)
		lines[editLine] = newLine

def nop(args):
	pass

instr = {
	"cpy": copy,
	"inc": incr,
	"dec": decr,
	"mul": mult,
	"jnz": jump,
	"tgl": togl,
	"nop": nop
}

with open("input.txt", "r") as f:
	for line in f:
		lines.append(line.replace("\n", ""))

# Part 1
# -----------------------------
counter = 0

try:
	while currLine < len(lines):
		split = lines[currLine].split(" ")
		instr[split[0]](split[1:])
		counter += 1
		currLine += 1
except:
	for line in lines:
		print(line)
	print("DATA")
	for d in data:
		print(d)

with open("output_part1.txt", "w") as o:
	o.write(str(data["a"]))

print("Part1: " + str(data["a"]))

# Part 2
# -----------------------------
lines = []
with open("inputpt2.txt", "r") as f:
	for line in f:
		lines.append(line.replace("\n", ""))

currLine = 0
data = {"a": 12}

try:
	while currLine < len(lines):
		split = lines[currLine].split(" ")
		instr[split[0]](split[1:])
		counter += 1
		currLine += 1
except:
	for line in lines:
		print(line)
	print("DATA")
	for d in data:
		print(d)

with open("output_part2.txt", "w") as o:
	o.write(str(data["a"]))
