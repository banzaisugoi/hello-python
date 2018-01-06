import sys
import stdio
import math

x = float(sys.argv[1])
y = float(sys.argv[2])

r = math.hypot(x, y)
fi = math.atan2(y, x)

stdio.write('r = ')
stdio.write(r)
stdio.write(', fi = ')
stdio.write(fi)