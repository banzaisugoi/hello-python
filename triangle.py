#-----------------------------------------------------------------------
# triangle.py
#-----------------------------------------------------------------------

import stdio
import sys
import math

# Accept integers a, b and c as command-line arguments.
# If any of them >= sum of two others print False. Else
# print True. Testing for triangle possibility.

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = bool((a < (b + c)) and (b < (a + c)) and (c < (a + b)))

stdio.writeln(d)