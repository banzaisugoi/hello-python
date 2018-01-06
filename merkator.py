import sys
import stdio
import math

lambd0 = float(sys.argv[1])
lambd = float(sys.argv[2])
fita = float(sys.argv[3])

x = lambd - lambd0
y = 0.5 * math.log((1 + math.sin(fita)) / (1 - math.sin(fita)))

stdio.write(x)
stdio.write(', ')
stdio.writeln(y)