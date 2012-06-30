import random
import math

class antibody:
    chromosome = 64
    learning = 5
    guesses = 4
    threshold = 48
    def __init__( self ):
        random.seed()
        self.lastFitness = 0
        self.chromosome = random.getrandbits( antibody.chromosome ) 
        self.learning = random.getrandbits( antibody.learning )
        self.guesses = antibody.guesses
        self.threshold = antibody.threshold
    def hamdist( self, antigen ):
        diffs = 0
        ham = self.chromosome ^ antigen
        for ch in bin(ham):
            if ch == '1':
                diffs += 1
        return diffs
    def mutate( self ):
        flipChro = math.floor( (1-self.lastFitness)*antibody.chromosome )
        flipLearn = math.floor( self.lastFitness*antibody.learning )
        mask = 0
        while flipChro > 0:
            mask = (1<<random.randint(0,antibody.chromosome))^mask
            flipChro -= 1
        self.chromosome ^= mask
        mask = 0
        while flipLearn> 0:
            mask = (1<<random.randint(0,antibody.learning))^mask
            flipLearn -= 1
        self.learning ^= mask           
        return
    def learn( self, h ):
        learned = math.floor(random.random()*self.learning)
        if learned < (antibody.chromosome - h):
            return learned
        else:
            return (antibody.chromosome - h)
    def fitness( self, antigen ):
        h = self.hamdist( antigen )
        i = 0
        l = 0
        while ((h+l) < self.threshold) and (i < self.guesses):
            l = self.learn(h)
            i += 1
        if (h+l > self.threshold):
            return ((h+l-i*2)/antibody.chromosome)
        else:
            return 0
        
        

class ga:
    generations = 100
    population = 100
    antigens = 8
    threshold = 48
    def __init__( self ):
        self.bestFitness = 0.0
        self.worstFitness = 100.0
        self.avgFitness = 0.0
        self.generations = ga.generations
        self.threshold = ga.threshold
        self.population = [None] * ga.population
        self.antigens = [None] * ga.antigens
        for i, n in enumerate(self.population):
            self.population[i] = antibody()
        for i, n in enumerate(self.antigens):
            self.antigens[i] = random.getrandbits( 64 )
    def sort( self ):
        self.population.sort( lambda a,b: cmp(a.lastFitness,b.lastFitness) )
        return
    def mask( self, point ):
        # create bit mask from point
        mask = 0
        i = 0
        while i < point:
            mask = (mask<<1) + 1
            i += 1
        return mask
    def crossover( self, anti_1, anti_2 ):
        # crossover with random point
        x = antibody.chromosome
        crossover = random.randint(0, x)
        mask = self.mask(crossover)
        anti_a = (anti_1&(~mask))|(anti_2&mask)
        anti_b = (anti_1&mask)|(anti_2&(~mask))
        return [anti_a, anti_b]
    def breed( self ):
        # Create the new population from the survivors
        for antibody in self.population:
            antibody.mutate()
        return
    def select( self ):
        survivors = []
        self.avgFitness = 0.0
        self.bestFitness = 0.0
        self.worstFitness = 100.0
        n = 0
        for antibody in self.population:
            fitness = 0.0
            i = 0
            while i < len(self.antigens):
                fitness += antibody.fitness(self.antigens[i])
                i += 1
            fitness = fitness / i
            antibody.lastFitness = fitness
            #if fitness > self.threshold:
            survivors.append(antibody)
            if(fitness > self.bestFitness):
                self.bestFitness = fitness
            if(fitness < self.worstFitness):
                self.worstFitness = fitness
            self.avgFitness += fitness
            n += 1
        self.avgFitness /= n
        return survivors
    def run( self ):
        i = 0
        while i < self.generations:
            #self.population = self.breed(self.select())
            self.population = self.select()
            self.breed()
            print 'generation %d' % i
            print 'best fitness: %f' % (self.bestFitness*100)
            print 'worst fitness: %f' % (self.worstFitness*100)
            print 'avg fitness: %f' % (self.avgFitness*100)
            print
            i += 1
        return self.population


ga = ga()
ga.run()

