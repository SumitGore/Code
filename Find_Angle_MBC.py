#Task
#  ABC is a right triangle, 90o at B.
#  Therefore, angle ABC = 90o.
#  Point M is the midpoint of hypotenuse AC.
#  You are given the lengths AB and BC.
#  Your task is to find angle MBC(angle theta, as shown in figure) in degrees.

import math

ab = int(input("Enter AB: "))
bc = int(input("Enter BC: "))
#ab = 10
#bc = 10
ac = math.sqrt((ab**2) + (bc**2))

c = math.degrees(math.atan(ab/bc))
a = math.degrees(math.atan(bc/ab))
mbc = math.degrees(math.atan2(ab,bc))
print("Mid Angle: ", round(mbc), chr(176), sep="")