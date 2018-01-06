#-----------------------------------------------------------------------
# division.py
#-----------------------------------------------------------------------

import stdio
import sys
import math

# Accept integers a and b as command-line arguments.
# If a % b == 0 print True.

a = int(sys.argv[1])
b = int(sys.argv[2])

c = bool((a % b) == 0)

stdio.writeln(c)
