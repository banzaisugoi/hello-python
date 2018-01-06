#-----------------------------------------------------------------------
# usethree.py
#-----------------------------------------------------------------------

import stdio
import sys

# Accept three names as a command-line argument. Write a message containing
# that names to standard output in backward order.

stdio.write('Hi, ')
stdio.write(sys.argv[3])
stdio.write(', ')
stdio.write(sys.argv[2])
stdio.write(' and ')
stdio.write(sys.argv[1])
stdio.writeln('. How are you?')

#-----------------------------------------------------------------------

# python usethree.py Alice Bob Carol
# Hi, Carol, Bob and Alice. How are you?
