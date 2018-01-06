import random
import stdio

a = random.random()
b = random.random()
c = random.random()
d = random.random()
e = random.random()

average = ((a + b + c + d + e) / 5.0)
maximum = max(a, b, c, d, e)
minimum = min(a, b, c, d, e)

stdio.writeln(a)
stdio.writeln(b)
stdio.writeln(c)
stdio.writeln(d)
stdio.writeln(e)

stdio.write('Average = ')
stdio.writeln(average)

stdio.write('Maximum = ')
stdio.writeln(maximum)

stdio.write('Minimum = ')
stdio.writeln(minimum)