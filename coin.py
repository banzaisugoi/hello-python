# --------------------------------------------------------------------------------------------
# coin.py
# --------------------------------------------------------------------------------------------

import stdio
import random

stdio.writeln()
stdio.writeln("Let's through a coin!")
stdio.writeln()

coin = int(random.randrange(1, 100))

if coin <=  50:
    stdio.writeln('Heads!')
else:
    stdio.writeln('Tails')
