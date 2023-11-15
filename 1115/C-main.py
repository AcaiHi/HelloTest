from C_1 import *
from C_2 import *

def cylinder(r, h):
  return cycle(r) * 2 + rectangle(2*r*3.14, h)

r = int(input('Please enter the radius of the cylinder: '))
h = int(input('Please enter the height of the cylinder: '))
print(cylinder(r, h))