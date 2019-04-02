import random 
def rollDie():
    """Returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])

print(rollDie())
 

def rollN(n):
    result = ''
    for i in range(n):
        result = result + str(rollDie())+" "
    print (result)
rollN(10)


def flip(numFlips):
    heads = 0.0
    for i in range(numFlips):
        if (random.random() < 0.5):
            heads += 1
    return heads/numFlips
print(flip(100))

 
def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    return mean
print(flipSim(2,10))


def flipPlot(minExp, maxExp):
    """Assumes minExp and maxExp positive integers; minExp < maxExp
Plots results of 2**minExp to 2**maxExp coin flips"""
    ratios = []
    diffs = []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
        for numFlips in xAxis:
            numHeads = 0
            for n in range(numFlips):
                if random.random() < 0.5:
                    numHeads += 1
                    numTails = numFlips - numHeads
                    ratios.append(numHeads/float(numTails))
                    diffs.append(abs(numHeads - numTails))
pylab.title('Difference Between Heads and Tails')
pylab.xlabel('Number of Flips')
pylab.ylabel('Abs(#Heads - #Tails)')
pylab.plot(xAxis, diffs)
pylab.figure()
pylab.title('Heads/Tails Ratios')
pylab.xlabel('Number of Flips')
pylab.ylabel('#Heads/#Tails')
pylab.plot(xAxis, ratios) 
 
random.seed(0)
flipPlot(4, 20) 
