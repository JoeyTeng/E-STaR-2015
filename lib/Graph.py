import networkx

class Graph(object):

    def __init__(self, level_increment = None):
        self.initialize(level_increment)
        
    """
        level_configuration = numpy.array(level_configuration)
        self.total_level = level_configuration.shape[0]
        self.level_index = numpy.array(numpy.zeros(self.total_level))
        tmp = 0
        sum = 0
        for level in range(1, self.total_level):
            tmp += level_configuration[level - 1]
            self.level_index[level] = self.level_index[level - 1] + tmp

        self.total_species = self.level_index[-1] + level_configuration[-1]
        self.web = numpy.matrix(numpy.zeros((self.total_speices, self.total_speices)))
"""

    def initialize(self, level_increment = None):
        self.data = networkx.DiGraph()
        self.level_index = [0] # Level 0 is Nothing
        self.total_species = 0
        current_level = 0
        for increment in level_increment:
            self.level_index.append(self.total_species + 1) # Number of Species until last level
            current_level += increment
            self.total_species += current_level
        self.data.add_nodes_from(xrange(1, self.total_species + 1))

    def basic_edges(self):
        pass
   
    def Generate_edges(self, Possibility = 0):
        pass

    def Add_edges(self, Possibility = (lambda(x): 0)):
        pass

    def swap_edge(self, x, y):
        pass

