#Matcher
#--coding:utf-8--

import networkx as nx
import matplotlib.pyplot as plt

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

def Reading(path):
    Graph = {}
    input = open(path, 'rb')
#    level = {}

    for line in input:
        Point = {}
        content = line.split(' ')
        Point['level'] = int(content[1])
        for point in content[2:]:
            Point[int(point)] = 1
        Graph[int(content[0])] = Point
#        try:
#            level[int(content[1])].append(int(content[0]))
#        except KeyError, ErrInfo:
#            level[ErrInfo[0]] = [int(content[0])]
        
    return Graph#, level

def Match(i, j):
    if len(Graph[i]) == 0:
        return 1

def Topological_Sorting(Graph):
    OutDegree = {}
    Sequence = []
    for item in Graph.iteritems():
        if (type(item[0]) == 'int'):
            OutDegree[item[0]] = len(item[1])
    while (len(Sequence < len(OutDegree))):
        Quene = []
        for point in range(0, len(OutDegree)):
            if (OutDegree[point] == 0):
                Quene.append(point)
        for point in Queue:
            Sequence.append(point)
            for item in Graph.iteritems():
                if (point in item[1]):
                    OutDegree[item[0]] -= 1

    return Sequence

def PreProcess(Graph):
    
    return

def Process():

    return

#--main--

Process()
