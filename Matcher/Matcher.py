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

def Process():
    return

#--main--

Process()
