# ------------------------------------------------------------------
# trigon.py
# ------------------------------------------------------------------

# proof that for any number as argument, function sin2(fi) + cos2(fi)
# gives answer 1.0 (always). Exercise 1.2.2 from book


import stdio
import sys
import math

fi = float(sys.argv[1])

answer = (math.sin(fi) ** 2) + (math.cos(fi) ** 2)

stdio.writeln(answer)
