import sys
import stdio
import math

t = float(sys.argv[1])
P = float(sys.argv[2])
r = float(sys.argv[3])

summa = P * (math.e ** (r * t))

stdio.writeln(summa)