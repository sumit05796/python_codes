radius = float(input('Enter Radius: '))
import math
pi = math.pi
area_circle = pi*radius**2
print(area_circle)

rectangle = input('Enter length and breadth separted by spaces: ')
length = float(rectangle.split()[0])
breadth = float(rectangle.split()[1])
area_rectangle = length*breadth
print(area_rectangle)
