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
error = []

big_per = 0
small_per = 0
both = False
i = 0

file = open("GDdata.txt")
content = file.readlines()

changes = len(content) - 2

for line in content:
    current_per = float(content[i].split(" ")[-1].strip("\n"))
    if "100" not in line:
        next_per = float(content[i + 1].split(" ")[-1].strip("\n"))

    if current_per > next_per:
        error.append(f"line {i + 1}: {line}")

    if "square" in line:
        square += next_per - current_per

    if "wave" in line:
        wave += next_per - current_per

    if "ship" in line:
        ship += next_per - current_per

    if "robot" in line:
        robot += next_per - current_per

    if "ufo" in line:
        ufo += next_per - current_per

    if "ball" in line:
        ball += next_per - current_per

    if "spider" in line:
        spider += next_per - current_per

    i += 1

for line in content:
    if "undual" in line:
        next_per = float(line.split(" ")[-1].strip("\n"))
        dual += next_per - current_per

    elif "dual" in line and "undual" not in line:
        current_per = float(line.split(" ")[-1].strip("\n"))

for line in content:
    if "big" in line and "small" not in line:
        big_per = float(line.split(" ")[-1].strip("\n"))
        small += big_per - small_per

        if both == True:
            big += big_per - small_per
            both = False

    elif "small" in line and "big" not in line:
        small_per = float(line.split(" ")[-1].strip("\n"))
        big += small_per - big_per

        if both == True:
            small += small_per - big_per
            both = False

    elif "big" in line and "small" in line:
        both = True

        if big_per > small_per:
            small_per = float(line.split(" ")[-1].strip("\n"))
            big += small_per - big_per
            big_per = float(line.split(" ")[-1].strip("\n"))

        else:
            big_per = float(line.split(" ")[-1].strip("\n"))
            small += big_per - small_per
            small_per = float(line.split(" ")[-1].strip("\n"))

for i in error:
    i = i.strip("\n")
    print(i)

if error == []:
    length = input("Level length (m:ss): ")
    seconds = (int(length.split(":")[0]) * 60) + int(length.split(":")[1])
    cpm = int(changes) / (int(seconds) / 60)

    print("")
    print(f"square: {round(square, 1)}%")
    print(f"ship: {round(ship, 1)}%")
    print(f"wave: {round(wave, 1)}%")
    print(f"robot: {round(robot, 1)}%")
    print(f"ufo: {round(ufo, 1)}%")
    print(f"ball: {round(ball, 1)}%")
    print(f"spider: {round(spider, 1)}%")
    print(f"dual: {round(dual, 1)}%")
    print(f"small: {round(small, 1)}%")
    print(f"big: {round(big, 1)}%")
    print(f"changes: {changes}")
    print(f"length: {seconds} sec")
    print(f"changes/min: {round(cpm, 1)}")
    print("")

while error == []:
    save = input("Save? y/n: ")

    if save == "y":
        name = input("Level name: ")
        with open("data.txt", "a") as file:
            file.write(f"{name}:\n")
            file.write(f"square: {round(square, 1)}%\n")
            file.write(f"ship: {round(ship, 1)}%\n")
            file.write(f"wave: {round(wave, 1)}%\n")
            file.write(f"robot: {round(robot, 1)}%\n")
            file.write(f"ufo: {round(ufo, 1)}%\n")
            file.write(f"ball: {round(ball, 1)}%\n")
            file.write(f"spider: {round(spider, 1)}%\n")
            file.write(f"dual: {round(dual, 1)}%\n")
            file.write(f"small: {round(small, 1)}%\n")
            file.write(f"big: {round(big, 1)}%\n")
            file.write(f"changes: {changes}\n")
            file.write(f"length: {seconds} sec\n")           
            file.write(f"changes/min: {round(cpm, 1)}\n\n")
            print(f"Saved {name}!")

        with open("changes.txt", "a") as file:
            file.write(f"{name}:\n")
            for line in content:
                file.write(f"{line}")
            file.write("\n\n")
        break

    elif save == "n":
        print("Exiting without saving.")
        break