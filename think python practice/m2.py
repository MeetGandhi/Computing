import math
signalpower=input('signal power=')
noisepower=input('noise power=')
decibels=10*math.log10(signalpower/noisepower)
print 'decibals=',decibels
