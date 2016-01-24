#Simulation via formula, parameter of vectors and matrixes.
#--coding:utf-8--
import copy

class dataClass(object):
    #Vectors:
    Population = [] #n
    IntrinsicGrowthRate = [] #µ
    MaxPopulation = [] #N
    DeathRate = [] #λ
    ConversionRate = [] #s, σ
    #Matrixes:
    HistoryPopulation = [] #n(t)
    PredationEfficiency = [] #A, α
    def __init__(self):
        pass
    
    def initialize(self, Graph):
        self.Population = [0] + [-1] * Graph['total']
        self.IntrinsicGrowthRate = [0] + [0] * (Graph['total'] - len(Graph['level%d' %(Graph['level'] - 1)])) + [-1] * (len(Graph['level%d' %(Graph['level'] - 1)]))
        self.MaxPopulation = copy.deepcopy(self.IntrinsicGrowthRate)
        self.DeathRate = copy.deepcopy(self.Population)
        self.ConversionRate = [0] + [-1] * (Graph['total'] - len(Graph['level%d' %(Graph['level'] - 1)])) + [0] * (len(Graph['level%d' %(Graph['level'] - 1)]))
        self.HistoryPopulation = []

        self.PredationEfficiency = [0] * (Graph['total'] - len(Graph['level%d' %(Graph['level'] - 1)])) + [0] * (len(Graph['level%d' %(Graph['level'] - 1)]) + 1)
        tmp =  copy.deepcopy(self.PredationEfficiency) 
        self.PredationEfficiency = []
        for i in xrange(0, (Graph['total'] + 1)):
            self.PredationEfficiency.append(copy.deepcopy(tmp))
        for predaterLevel in xrange(0, Graph['level']):
            for predater in Graph['level%d' %predaterLevel]:
                for prey in Graph[predater]:
                    self.PredationEfficiency[predater][prey] = -1


    def input(self):
        print "\nClone List:"
        cloneList = []
        CheckDict = {}
        initPop = []
        intGrRate = []
        deathRate = []
        converRate = []
        cloneList = map(eval, raw_input().split())
        if cloneList:
            initPop = map(eval, raw_input("\nInit Pop:").split())
            intGrRate = map(eval, raw_input("\nintGrRate:").split())
            deathRate = map(eval, raw_input("\nDeath Rate:").split())
            converRate = map(eval, raw_input("\nConversion Rate:").split())
            Addition = range(len(self.Population), len(self.Population) + len(cloneList))
            for i in xrange(0, len(Addition)):
                checkList[Addition[i]] = cloneList[i]
                checkList[cloneList[i]] = Addition[i]

        print "\nPopulation"
        for i in xrange(0, len(self.Population)):
            if (self.Population[i] == -1):
                self.Population[i] = float(raw_input("%d: " %i))
                #self.Population[i] = tmp
        for i in initPop:
            self.Population.append(i)

        for i in xrange(0, len(cloneList)):
            if self.IntrinsicGrowthRate[cloneList[i]] != -1:
                intGrRate[i] = 0
        print "\nIntrinsic Growth Rate"
        for i in xrange(0, len(self.IntrinsicGrowthRate)):
            if (self.IntrinsicGrowthRate[i] == -1):
                tmp = float(raw_input("%d: " %i))
                self.IntrinsicGrowthRate[i] = tmp #float(raw_input("%d: " %i))
        for i in intGrRate:
            self.IntrinsicGrowthRate.append[i]

        print "\nMax Population"
        for i in xrange(0, len(self.MaxPopulation)):
            if (self.MaxPopulation[i] == 0):
                self.MaxPopulation[i] = 1
            if (self.MaxPopulation[i] == -1):
                tmp = float(raw_input("%d: " %i))
                self.MaxPopulation[i] = tmp #float(raw_input("%d: " %i))
        for i in cloneList:
            self.MaxPopulation.append(self.MaxPopulation[cloneList[i]])

        print "\nDeath Rate"
        for i in xrange(0, len(self.DeathRate)):
            if (self.DeathRate[i] == -1):
                tmp = float(raw_input("%d: " %i))
                self.DeathRate[i] = tmp #float(raw_input("%d: " %i))
        for i in deathRate:
            self.DeathRate.append(i)

        print "\nConversion Rate"
        for i in xrange(0, len(self.ConversionRate)):
            if (self.ConversionRate[i] == -1):
                tmp = float(raw_input("%d: " %i))
                self.ConversionRate[i] = tmp #float(raw_input("%d: " %i))
        for i in converRate:
            self.ConversionRate.append(i)

        print "Predation Efficiency"
        for i in xrange(0, len(cloneList)):
            for j in self.PredationEfficiency:
                j.append(0)
        for i in xrange(0, len(cloneList)):
            self.PredationEfficiency.append([0] * len(self.PredationEfficiency[0]))
        for i in xrange(0, len(self.PredationEfficiency)):
            for j in xrange(0, len(self.PredationEfficiency[i])):
                if (self.PredationEfficiency[i][j] == -1):
                    tmp = float(raw_input("predator %d->%d: " %(i, j)))
                    self.PredationEfficiency[i][j] = tmp #float(raw_input("%d -> %d: " %(i, j)))
                    try:
                        self.PredationEfficiency[i][checkList[j]] = tmp
                    except:
                        pass
                    try:
                        self.PredationEfficiency[checkList[i]][j] = tmp
                    except:
                        pass

#Formula:
#n[i][t + 1] = n[i][t] - lambda[i]*n[i][t] + mu[i] * n[i][t] * (1 - n[i][t]/N[i]) 
#   + sigma[i] * SUM(1, j, lambda(i, j): alpha[i][j] * n[i][t] * n[j][t]) 
#   - SUM(i, j, lambda(i, j): alpha[j][i] * n[j][t] * n[i][t])
def Step(data):
    NewPopulation = [0]*len(data.Population)
    for i in xrange(1, len(data.Population)):
        """NewPopulation[i] = data.Population[i] - data.DeathRate[i] * data.Population[i]\
            + data.IntrinsicGrowthRate[i] * data.Population[i] * (1 - data.Population[i] / data.MaxPopulation[i])\
            + data.ConversionRate[i] * Sum(i, len(data.Population), (lambda(j): data.PredationEfficiency[i][j] * data.Population[i] * data.Population[j]))\
            - Sum(len(data.Population), (lambda(j): data.PredationEfficiency[j][i] * data.Population[j] * data.Population[i]))"""
        a = data.DeathRate[i] * data.Population[i]
        b = data.IntrinsicGrowthRate[i] * data.Population[i] * (1 - data.Population[i] / data.MaxPopulation[i])
        c = data.ConversionRate[i] * Sum(i, len(data.Population), (lambda(j): data.PredationEfficiency[i][j] * data.Population[i] * data.Population[j]))
        d = Sum(0, i, (lambda(j): data.PredationEfficiency[j][i] * data.Population[j] * data.Population[i]))
        NewPopulation[i] = data.Population[i] - a + b + c - d
        NewPopulation[i] = max(NewPopulation[i], 0)
#        print "History %r; Death %r; Grow %r; Eat %r; Eaten %r" %(data.Population[i], a, b, c, d)

    return NewPopulation

def Sum(minimum, maximum, expression):
    Ans = 0
    for j in xrange(minimum, maximum):
        Ans += expression(j)

    return Ans

def Calculation(data, Steps):
    print "\nRunning %d steps" %Steps
    data.HistoryPopulation.append(data.Population)
    for t in xrange(0, Steps):
        data.Population = data.HistoryPopulation[t]
        data.HistoryPopulation.append(Step(data))

    return data.HistoryPopulation

def main(Graph):
    data = dataClass()
    data.initialize(Graph)
    data.input()

    print "Population\n", data.Population
    print "IG:\n", data.IntrinsicGrowthRate
    print "Max:\n", data.MaxPopulation
    print "Death:\n", data.DeathRate
    print "Conv:\n", data.ConversionRate
    print "His:\n", data.HistoryPopulation
    print "Matrix:\n"
    for line in data.PredationEfficiency:
        print line

    print ""

    return Calculation(data, int(raw_input('Please input steps of simulation:')))


#--main--

if __name__ == '__main__':
    main()
