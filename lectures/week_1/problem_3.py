def loadFile():
    PATH = 'C:\Users\Nate\Documents\edx-6.00.2x-problem-sets\lectures\week_1\julyTemps.txt'
    inFile = open(PATH)
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)
    
def producePlot(lowTemps, highTemps):
    import pylab
    diffTemps = []
    for low, high in zip(lowTemps, highTemps):
        diffTemps.append(high - low)
        
    pylab.plot(range(1, 32), lowTemps)
    pylab.plot(range(1, 32), highTemps)
    pylab.plot(range(1, 32), diffTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()