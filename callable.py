import __init__
import sys

def OutputErr(content):
    sys.stdout, sys.stderr = sys.stderr, sys.stdout
    print content
    sys.stdout, sys.stderr = sys.stderr, sys.stdout

def main():

#    OutputErr("Start Graph")
    Graph1 = __init__.Generator.main("Graph1")
#    OutputErr("Fin")
    #Graph2 = __init__.Generator.main("Graph2")

    #match = __init__.Match.Default(Graph1, Graph2)

#    OutputErr("Start Simulate")
    History = __init__.Simulation.main(Graph1)
#    OutputErr("Fin")
    output = open("data.csv", 'wb')
    print ""

#    OutputErr("Start Check")
    print "Period ", __init__.CircleChecker.main(History), '\n'
#    OutputErr("Fin")

#    OutputErr("Start Output")
    for line in History:
        print line[1:]
        for i in line[1:]:
            output.write("%r," %i)
        output.write('\n')
#    OutputErr("Fin")

if __name__ == "__main__":
    main()
