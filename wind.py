import sys
import stdio

t = float(sys.argv[1])
v = float(sys.argv[2])

w = 35.74 + (0.6215 * t) + ((v ** 0.16) * ((0.4275 * t) - 35.75))

stdio.writeln(w)
