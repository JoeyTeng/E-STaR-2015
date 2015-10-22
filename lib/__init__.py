"""
lib:
    Library

__init__.py:
    import classes

Class.py:
    import all classes.

Graph.py:
    Codes about class 'Graph'
    
    Modules used:
        networkx

    Logic Structure:
        Direct Graph by Level.
        Extend from Tree:
            Allow cross-level edge
            Allow one node with mutiple predecessor
            Disallow one node have a successor from a higher level

    Construct:
        array of increment of number of species down by level

"""

from Class import *
