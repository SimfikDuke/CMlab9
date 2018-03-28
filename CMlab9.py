from numpy import linalg as la
import numpy as np
from det import det

a = [[2, 3],
     [1, 4]]  # Start matrix

e = 1e-2  # Epsilon

d = det(a, False)  # Max = False, Min = True
d.epscals(e)
