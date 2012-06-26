import random

def hamdist(str1, str2):
    diffs = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            diffs += 1
    return diffs

random.seed()
popSize = 100
i = 0
x = [0] * popSize


while i < popSize:
    #print 'random: ' + str(random.getrandbits(64))
    x[i] = random.getrandbits(32)
    i += 1

m = bin(x[0])[2:64].rjust(64,'0')
n = bin(x[1])[2:64].rjust(64,'0')
o = bin(x[0]^x[1])[2:64].rjust(64,'0')
print m
print n
print o
print hamdist( m,n )