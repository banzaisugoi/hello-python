import sys
import stdio

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

order = bool((x < y < z) or (x > y > z))

stdio.writeln(order)