from __init__ import *

Graph1 = Generator.main("Graph1")
#Graph2 = Generator.main("Graph2")

#match = Matcher.Default(Graph1, Graph2)

History = Simulation.main(Graph1)
output = open("data.csv", 'wb')
print ""

print "Period ", CircleChecker.main(History), '\n'

for line in History:
    print line[1:]
    for i in line[1:]:
        output.write("%r," %i)
    output.write('\n')


