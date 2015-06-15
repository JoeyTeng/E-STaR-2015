#Generator.py
#--coding:utf-8--

import random
import networkx as nx
import matplotlib.pyplot as plt
import re

def GetInput(TransferFunction, String):
    while True:
        string = raw_input(String)
        try:
            if (re.search(r'[\S]*', string).group(0) == 'None'):
                print '####None####'
                return None
            return TransferFunction(string)
        except ValueError:
            pass

def GetList(Now, Next, Cross, All, PossibilityCross):
    print "GetList Now %r, Next %r, Cross %r, All %r, Poss %r" %(Now, Next, Cross, All, PossibilityCross)
    if (Cross == None):
        return range(Now + Next, All)
    NextList = range(Now + Next, Now + Next + Cross)
    CrossList = range(Now + Next + Cross, All)
    try:
        nSampleNextList = min(
                            len(CrossList) * (1 - PossibilityCross) / PossibilityCross,
                            len(NextList))
    except ZeroDivisionError:
        nSampleNextList = len(NextList)
    try:
        nSampleCrossList = nSampleNextList * PossibilityCross / (1 - PossibilityCross)
    except ZeroDivisionError:
        nSampleCrossList = len(CrossList)
#    print 'Next %r, Cross %r, All %r, Poss %r\nnNext %r, nCross %r\nNext %r\nCross %r' %(Next, Cross, All, PossibilityCross, nSampleNextList, nSampleCrossList, NextList, CrossList)
    return random.sample(NextList, int(nSampleNextList)) +\
           random.sample(CrossList, int(nSampleCrossList))

def Generator(NumberSpecies, Width, Depth, PossibilityCross = None, Mean = None, StandardDeviation = None, First = None):
    Graph = {}
    if PossibilityCross == None:
        PossibilityCross = 0.5
    if PossibilityCross > 1:
        PossibilityCross = 1
    if PossibilityCross < 0:
        PossibilityCross = 0
    Graph['PossibilityCross'] = PossibilityCross

    if Mean == None or Mean < 0:
        Mean = Width / 2
        Graph['Mean'] = Mean
    if StandardDeviation == None or StandardDeviation < 0:
        StandardDeviation = Width ** 2
    Graph['StandardDeviation'] = StandardDeviation
    Variance = (StandardDeviation ** 2) * NumberSpecies
    Graph['Variance'] = Variance

    Graph['Depth'] = 0
    if First > NumberSpecies:
        First = None
    if First != None:
        Graph['level0'] = First
        Graph['Depth'] = 1

    print "NumberSpecies %r\nWidth %r\nDepth %r\nPossibilityCross %r\nMean %r\nStandardDeviation%r\n"\
        %(NumberSpecies, Width, Depth, PossibilityCross, Mean, StandardDeviation)

    NS = NumberSpecies
    Graph['Total'] = NumberSpecies
    while NS > 0 and Graph['Depth'] < Depth:#Devide trophic level
        try:
            Graph['level' + str(Graph['Depth'])] = random.randint(1, min(Width * Graph['level' + str(Graph['Depth'] - 1)], NS))
        except KeyError:
            Graph['level' + str(Graph['Depth'])] = random.randint(1, NS)
        NS -= Graph['level' + str(Graph['Depth'])]
        Graph['Depth'] += 1
    if Graph['Depth'] == Depth and NS != 0:
        Graph['level' + str(Graph['Depth'])] = NS
        Graph['Depth'] += 1
    Graph['level' + str(Graph['Depth'])] = None

    Graph['Width'] = 0
    for i in range(0, Graph['Total']):
        Graph[i] = []
    tot = 0 #Generate the Prey-Predator relationship
    Now = 0 #Start No of current level
    for Deep in range(0, Graph['Depth'] - 1):
        for i in range(0, Graph['level' + str(Deep)]):
            TmpList = \
                        GetList(
                            Now,
                            Graph['level' + str(Deep + 1)],  #Next
                            Graph['level' + str(Deep + 2)],  #Cross
                            Graph['Total'],                  #All #Number of Nodes below the level
                            Graph['PossibilityCross'])
            print 'len %r, Mean %r, Variance %r, TmpList %r' %(len(TmpList), Mean, Variance, None)#TmpList)
            if len(TmpList) != 0:
                Graph[tot] =\
                sorted(
                    random.sample(
                        TmpList,
                        random.randint(
                            max(0, Mean - Variance),         #Number must in [-Va + Mean, Va + Mean]
                            min(min(
                                    len(TmpList),            #Prevent Error: "Out of Range"
                                    Width),                  #Limit: Width
                                Mean + Variance)             #Limit: Mean & StandardDeviation
                        )
                    )
                )#Choose preys from down levels
            Variance -= (Mean - len(Graph[tot])) ** 2
            Graph['Width'] = max(Graph['Width'], len(Graph[tot]))
            tot += 1
        Now += Graph['level' + str(Deep)]

    return Graph

def Transfer(Graph):
    List = []
    for i in range(0, Graph['Total']):
        for j in Graph[i]:
            List.append((i,j))

    print "List %r" %List
    return List

def Pos(Graph):
    dictionary = {}
    No = 0
    for level in range(0, Graph['Depth']):
        for i in range(0, Graph['level' + str(level)]):
            dictionary[No] = (float(i) + level * 0.1, float(Graph['Depth'] - level))
            No += 1
    return dictionary

def Dic(begin, end):
    dictionary = {}
    for i in range(begin, end):
        dictionary[i] = i
    return dictionary

def Process():
    Width = GetInput(lambda(x):int(x), 'Width: \n')
    Depth = GetInput(lambda(x):int(x), 'Depth: \n')
    NumberSpecies = GetInput(lambda(x):int(x), 'Number of Species: \n')
    PossibilityCross = GetInput(lambda(x):float(x), 'Possibility of Cross-trophic level predation taking place (%): \n')
    Mean = GetInput(float, 'Mean: \n')#Mean of Width of each node
    StandardDeviation = GetInput(lambda(x):float(x), 'Standard Deviation of Width of the Species: \n')
    First = GetInput(int, 'Number of Nodes in First Level:\n')

    Graph = Generator(NumberSpecies, Width, Depth, PossibilityCross, Mean, StandardDeviation, First)
    
    print Graph

    graph = nx.DiGraph(Transfer(Graph))
    #Draw
#    print nx.spring_layout(graph)
    nx.draw_networkx(graph, pos = Pos(Graph))
    plt.savefig('Graph.png')
    plt.show()
#--main--
Process()
