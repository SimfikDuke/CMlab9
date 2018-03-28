from numpy import linalg as la
import numpy as np
from det import det

a = [[2,3],
     [1,4]]
e = 1e-2

d = det(a)
d.epscals(e)
