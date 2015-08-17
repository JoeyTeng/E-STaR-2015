#Matcher
#--coding:utf-8--

import re
import os
import networkx as nx
import matplotlib.pyplot as plt

class listConductor(object):
    def __init__(self, input):
        List = []
        item = ''
        quote = False
        dQuote = False
        comma = ','
        squareBracket = False
        bracket = False
        brace = False
        bSlant = False
        return self.Conductor(input)

    def Conductor(self, input):
        index = 0
        Ans = None
        while index < len(input):
            if input[index] == '\\':
                self.BSlant(input[index:])
            elif input == '"' or "'":
                ans = str(self.Quote(input[index:]))
            elif input == ',':
                List.append(self.item)
            else:
                pass
            index += 1

        return self.List

    def BSlant(input):
        switcher = {
                'n': '\n',
                'r': '\r',
                'b': '\b',
                'a': '\a',
                '"': r'\"',
                "'": r"\'"
                }

        try:
            self.item += switcher[input[0] + 1]
        except KeyError, ErrInfo:
            self.item += ErrInfo

        self.bSlant = False
        return


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

def TypeAbstract(input):
    return re.search(r"(?<=').+(?=')", input)

def GetConstructor(type):
    if type == 'int':
        return int
    if type == 'long':
        return long
    if type == 'float':
        return float
    if type == 'str':
        return str
    if type == 'bool':
        return bool
#    if type == 'tuple':
#        return tupleConductor
    if type == 'list':
        return listConductor
#    if type == 'dict':
#        return dictConductor
    return None

def Reading(path):
    Graph = {}
    input = open(path, 'rb')
#    level = {}
    
    Lines = input.readlines()
    for i in range(0, len(Lines) >> 2):
        typeKey = TypeAbstract(input[i << 2])
        typeValue = TypeAbstract(input[(1 << 2) + 1])
        s
#        Point = {}
#        content = line.split(' ')
#        Point['level'] = int(content[1])
#        for point in content[2:]:
#            Point[int(point)] = 1
#        Graph[int(content[0])] = Point
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
