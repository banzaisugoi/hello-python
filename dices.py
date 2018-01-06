# ------------------------------------------------------------------------------------------
# dices.py
# ------------------------------------------------------------------------------------------

# This program simulates throughint two dices and returns their random values.

import stdio
import random

dice1 = random.randrange(1, 6)
dice2 = random.randrange(1, 6)
summary = dice1 + dice2

stdio.writeln()
stdio.writeln("Let's through dices!")
stdio.writeln()

stdio.write('Dice #1: ')
stdio.writeln(dice1)

stdio.write('Dice #2: ')
stdio.writeln(dice2)

stdio.write('Their sum is ')
stdio.writeln(summary)

stdio.writeln()