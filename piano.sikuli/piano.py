"""
    Piano
    Written by: Gosia
    For: Geek Academy
"""

Settings.MoveMouseDelay = 0.1
App.open("c:\\Program Files\\Internet Explorer\\iexplore.exe")
sleep(2)
click(Pattern("1440525623002.png").targetOffset(-15,0))
sleep(2)
type("www.onlinepianist.com/virtual_piano")
type(Key.ENTER)
sleep(2)
for i in range(15):
    type(Key.DOWN)
click("1440526696964.png")
sleep(5)
red_point=find(Pattern("1440527279171.png").exact().targetOffset(0,-3))

x = red_point.x + 7
y = red_point.y + 5

notes = []
key_width = 28
for i in range(0, 8*key_width, key_width):
        note = Location(x + i, y)
        notes.append(note)

do = notes[0]
re = notes[1]
mi = notes[2]
fa = notes[3]
sol = notes[4]
la = notes[5]
si = notes[6]
do1 = notes[7]

#Oda do radosci
click(mi)
sleep(0.25)
click(mi)
sleep(0.25)
click(fa)
sleep(0.25)
click(sol)
sleep(0.25)
click(sol)
sleep(0.25)
click(fa)
sleep(0.25)
click(mi)
sleep(0.25)
click(re)
sleep(0.25)
click(do)
sleep(0.25)
click(do)
sleep(0.25)
click(re)
sleep(0.25)
click(mi)
sleep(0.25)
click(mi)
sleep(0.375)
click(re)
sleep(0.125)
click(re)

sleep(1)


