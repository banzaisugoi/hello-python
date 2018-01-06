import sys
import stdio

x0 = float(sys.argv[1])
v0 = float(sys.argv[2])
t = float(sys.argv[3])

G = 9.80665

result = (x0 + (v0 * t)) - ((G * t * t) / 2.0)

stdio.write('If x0 = ')
stdio.write(x0)
stdio.write(', v0 = ')
stdio.write(v0)
stdio.write(' and t = ')
stdio.write(t)
stdio.writeln(',')
stdio.writeln('For x0 + v0*t - (G*t^2)/2,')
stdio.write('the result is: ')
stdio.write(result)
stdio.writeln(' meters')