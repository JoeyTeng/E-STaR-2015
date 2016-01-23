#--coding:utf-8--
from sys import argv

class FoodWeb(object):
    pass

def GeneratorCounter(content):
    DeltaList = map(eval, content[0].split())
    print DeltaList
    count = 0
    level = [0]
    for i in DeltaList:
        level.append(level[-1] + i)
        count += level[-1]
    level = level[1:]
    return count, level

def Extracter(path):
    content = open(path, 'rb').readlines()
    print "Generator Part:"
    print content[:3]
    No, Level = GeneratorCounter(content[:3])
    print No, Level
    content = content[3:]

    print "Simulator Part:"
    print "Population:"
    print content[:No]
    Population = map(eval, content[:No])
    print Population
    content = content[No:]

    print "Intrinsic Growth Rate:"
    print content[:Level[-1]]
    IntrinsicGrowthRate = map(eval, content[:Level[-1]])
    print IntrinsicGrowthRate
    content = content[Level[-1]:]

    print "Max Population:"
    print content[:Level[-1]]
    MaxPopulation = map(eval, content[:Level[-1]])
    print MaxPopulation
    content = content[Level[-1]:]

    print "Death Rate:"
    print content[:No]
    DeathRate = map(eval, content[:No])
    print DeathRate
    content = content[No:]

    print "Conversion Rate:"
    print content[:No - Level[-1]]
    ConversionRate = map(eval, content[:No - Level[-1]])
    print ConversionRate
    content = content[No - Level[-1]:]

    print "Predation Efficiency"
    print content[:-1]
    PredationEfficiency = map(eval, content[:-1])
    print PredationEfficiency
    content = content[-1:]

    print "Steps:"
    print content
    Steps = eval(content[0])
    print Steps
    content = []

    result = FoodWeb()
    result.No = No
    result.Level = Level
    result.Population = Population
    result.IntrinsicGrowthRate = IntrinsicGrowthRate
    result.MaxPopulation = MaxPopulation
    result.DeathRate = DeathRate
    result.ConversionRate = ConversionRate
    result.PredationEfficiency = PredationEfficiency

    return result

if __name__ != "__main__":
    raise EnvironmentError("Please Run Directly!")
else:
    Extracter(argv[1])
