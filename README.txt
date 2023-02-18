
This is the data Jeyzor collected for his video "Game Mode Usage in the Top 10 Demons in Geometry Dash (Graph Race)".

CONTENTS:
level calc.py is a python program that calculates the stats for a single level.
average calc.py is a python program that calculates the average stats from a collection of levels.
GDdata.txt is a text file that these programs use for the calculations.

game mode changes.txt is a text file that includes all of the game mode changes for every level that has been in the top 10 (up until February 2023).
level data.txt is a text file that stores the stats for every individual level that has been in the top 10 (up until February 2023).
top 10 graph.xlsx is an excel file that shows the timeline for all changes in the top 10 (up until February 2023).


HOW TO CALCULATE AN INDIVIDUAL LEVEL'S STATS:
1. Download level calc.py and GDdata.txt
2. Open GDdata.txt
3. Type the wanted game mode changes in GDdata.txt
4. Save the file
5. Open and run level calc.py
6. Save the stats if you want to store them to calculate the average of multiple levels

How to type game mode changes in GDdata.txt:
The syntax should be:
<dual/undual> <big/small> <game mode(s)> <percentage>
The first three elements can be in any order but percentage must be the last element in the line

-every line must have the game mode name
-every line must have the percentage of the game mode's change at the end of line without the % sign
-if the size changes, it must be in the line ("small" or "big")
-the first line must have the size
-if a dual starts, "dual" must be in the line and "undual" if a dual ends
-during a dual with big and small size, both words must be in the line
-during a dual with two different game modes, both game mode names must be in the line
-the last line must be "small 100" if the level ends on big size or "big 100" if the level ends on small size
 or "undual small/big 100" if the level ends during a dual
-every element must be separated with a space

game mode names the program tracks:
square
ship
wave
robot
ufo
ball
spider

example GDdata.txt contents:
small square 0
ufo 10
big dual ufo 19.9
dual ufo 24.4
big small ufo 46
ship spider 47.7
big ship spider 67
undual ball 80
small ball 87.3
big ball 89
small ship 95.4
big 100


HOW TO CALCULATE THE AVERAGE STATS OF MULTIPLE LEVELS:
1. Download level data.txt, average calc.py and GDdata.txt
2. Open GDdata.txt and type the levels you want to calculate the average of
3. Save the file
4. Open and run average calc.py

How to type the levels you want to calculate the average of:
Each line must be only one level's name (case sensitive)

Example GDdata.txt contents:
Kenos
Yatagarasu
ZAPHKIEL
