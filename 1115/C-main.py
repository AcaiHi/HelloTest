from C_1 import *
from C_2 import *

def cylinder(r, h):
  return cycle(r) * 2 + rectangle(2*r*3.14, h)

print(cylinder(2, 3))