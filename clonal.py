import random

# GLOBALS
GEN = 1000
POP = 100
GUESS = 5
THRESHOLD = 16

# functions
def hamdist(str1, str2):
    '''Stole from ActiveState, not the most efficient hamming distance function ever...'''
    diffs = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            diffs += 1
    return diffs

def initPop( size ):
    i = 0
    population = [0] * size
    random.seed()
    while i < size:
        #print 'random: ' + str(random.getrandbits(64))
        population[i] = random.getrandbits(32)
        i += 1
    return population

def breed( pop ):
    # spawn new children with some rule?
    return

def fitness( antibody, antigen ):
    # Something should be happening here with guessing on the antibodies part
    # antibody and antigen should be integers
    m = bin(antibody[0])[2:64].rjust(64,'0')
    n = bin(anitgen[1])[2:64].rjust(64,'0')
    return hamdist( m,n )

def replace( pop, antigen ):
    for i, member in pop:
        val = fitness( member, antigen )
        if val < THRESHOLD:
            x[i] = 123 #new?  This is where mutation should happen
    return pop

def ga(pop, gen):
    i = 0
    antigen = 99 #???
    while i < gen:
        replace( pop, antigen )
        i += 1
        

m = bin(x[0])[2:64].rjust(64,'0')
n = bin(x[1])[2:64].rjust(64,'0')
o = bin(x[0]^x[1])[2:64].rjust(64,'0')
print m
print n
print o
print hamdist( m,n )
