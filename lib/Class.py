import numpy

class Graph(object):
    def __init__(self, level_configuration = [0]):
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


