import __init__

def main():

    Graph1 = __init__.Generator.main("Graph1")
    #Graph2 = __init__.Generator.main("Graph2")

    #match = __init__.Match.Default(Graph1, Graph2)

    History = __init__.Simulation.main(Graph1)
    output = open("data.csv", 'wb')
    print ""

    print "Period ", __init__.CircleChecker.main(History), '\n'

    for line in History:
        print line[1:]
        for i in line[1:]:
            output.write("%r," %i)
        output.write('\n')

if __name__ == "__main__":
    main()
