import numpy
import talib
c = numpy.random.random(100)
s = talib.SMA(c)
print(s)