#Generator.py
#--coding:utf-8--

import random
import networkx
import matplotlib.pyplot as plt

def GetInput(TransferFunction, String):
    while True:
        try:
            return TransferFunction(raw_input(String))
        except ValueError:
            pass

def Generator(NumberSpecies, Width, Depth, PossibilityCross = None, Mean = None, StandardDeviation = 0.0):
    if Mean == None:
        Mean = Width / 2
    Graph = {'Depth': 0}
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

    Graph['Width'] = 0
    for i in range(0, Graph['Total']):
        Graph[i] = []
    tot = 0 #Generate the Prey-Predator relationship
    for Deep in range(1, Graph['Depth'] - 1):
        for i in range(0, Graph['level' + str(Deep)]):
            Graph[tot] =\
                sorted(\
                    random.sample(\
                        xrange(Graph['level' + str(Deep + 1)], Graph['Total']),\
                        random.randint(0,\
                            min(Graph['Total'] - Graph['level' + str(Deep + 1)], Width)\
                        )\
                    )\
                )#Choose preys from down levels
            Graph['Width'] = max(Graph['Width'], len(Graph[tot]))
            tot += 1

    return Graph

#--main--
Width = GetInput(lambda(x):int(x), 'Width: \n')
Depth = GetInput(lambda(x):int(x), 'Depth: \n')
NumberSpecies = GetInput(lambda(x):int(x), 'Number of Species: \n')
PossibilityCross = GetInput(lambda(x):float(x), 'Possibility of Cross-trophic level predation taking place (%): \n')
Mean = GetInput(float, 'Mean: \n')
StandardDeviation = GetInput(lambda(x):float(x), 'Standard Deviation of Width of the Species: \n')

Graph = Generator(NumberSpecies, Width, Depth, PossibilityCross, Mean, StandardDeviation)
print Graph
