file = open("level data.txt")
content = file.readlines()
content_strip = [i.strip(":\n") for i in content]
square = 0
ship = 0
wave = 0
robot = 0
ufo = 0
ball = 0
spider = 0
dual = 0
big = 0
small = 0
changes = 0
length_sec = 0
levels = []

file2 = open("GDdata.txt")
levelfile = file2.readlines()

for i in levelfile:
    i = i.strip("\n")
    levels.append(i)

for level in levels:
    i = content_strip.index(level)

    square += float(content[i + 1].split()[1].split("%")[0])
    ship += float(content[i + 2].split()[1].split("%")[0])
    wave += float(content[i + 3].split()[1].split("%")[0])
    robot += float(content[i + 4].split()[1].split("%")[0])
    ufo += float(content[i + 5].split()[1].split("%")[0])
    ball += float(content[i + 6].split()[1].split("%")[0])
    spider += float(content[i + 7].split()[1].split("%")[0])
    dual += float(content[i + 8].split()[1].split("%")[0])
    small += float(content[i + 9].split()[1].split("%")[0])
    big += float(content[i + 10].split()[1].split("%")[0])
    changes += int(content[i + 11].split()[1])
    length_sec += int(content[i + 12].split()[1])

cpm = float(changes / (length_sec / 60))
length_avg_sec = round(length_sec / len(levelfile))
length_min = 0
length_avg_min = 0

while length_sec >= 60:
    length_min += 1
    length_sec -= 60

if length_sec < 10:
    length_sec = f"0{length_sec}"

while length_avg_sec >= 60:
    length_avg_min += 1
    length_avg_sec -= 60

if length_avg_sec < 10:
    length_avg_sec = f"0{length_avg_sec}"

print("")
print("Average:")
print(f"square: {round(square / len(levelfile), 1)}%")
print(f"ship: {round(ship / len(levelfile), 1)}%")
print(f"wave: {round(wave / len(levelfile), 1)}%")
print(f"robot: {round(robot / len(levelfile), 1)}%")
print(f"ufo: {round(ufo / len(levelfile), 1)}%")
print(f"ball: {round(ball / len(levelfile), 1)}%")
print(f"spider: {round(spider / len(levelfile), 1)}%")
print(f"dual: {round(dual / len(levelfile), 1)}%")
print(f"small: {round(small / len(levelfile), 1)}%")
print(f"big: {round(big / len(levelfile), 1)}%")
print(f"changes: {round(changes / len(levelfile), 1)}")
print(f"length: {length_avg_min}:{length_avg_sec}")
print(f"changes/min: {round((cpm), 1)}")