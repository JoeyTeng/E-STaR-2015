#Generater a Food web
#Output by a JPEG and a File

from PIL import Image
from PIL import ImageDraw
import random
import re

def Read():
    List = []
    for num in re.search(r'(?:[\S]+.*[\S])|(?:[\S]+)', re.sub(r'[ ]+', ' ', raw_input("delta list\n"))).group(0).split(' '):
        List.append(int(num))

    return List

def Generate(List):
    Graph = {}
    Graph['level'] = 0
    Graph['total'] = 0
    prev = 0
    for delta in List:
        Graph['level%d' %Graph['level']] = range(Graph['total'] + 1, Graph['total'] + delta + prev + 1)
        for point in Graph['level%d' %Graph['level']]:
            Graph[point] = []
        Graph['total'] += prev
        Graph['total'] += delta
        prev = len(Graph['level%d' %Graph['level']])
        Graph['level'] += 1
    Graph['level%d' %Graph['level']] = [Graph['total']]

    for level in range(0, Graph['level'] - 1):

        next = Graph['level%d' %(level + 1)][0]
        maximum = Graph['level%d' %(level + 1)][-1]
        Range = len(Graph['level%d' %(level + 1)])

        begin = Graph['level%d' %level][0]
        NumOfLevel = len(Graph['level%d' %level])
        End = max(3, ((maximum - next + NumOfLevel - 1) / NumOfLevel) + 1)

        present = next
        for point in Graph['level%d' %level]:

            PreyList = []
            end = min(End, Range)
            for delta in range(0, end):
                PreyList.append(((present + delta) - next) % Range + next)

            present = (present + end - next) % Range + next

            Graph[point] = PreyList
            #Graph[point] = range(next + point - begin, min((next + point - begin + 3), maximum) + 1)
    print "Generated", Graph
    return Graph

def RandSwap(Graph, percentage):
    for level in range(0, Graph['level']):
        for i in Graph['level%d' %level][:-1]:
            for j in (i + 1, Graph['level%d' %(level + 1)][0] - 1):
                #print Graph[i], Graph[j]
                for k in range(0, len(Graph[i])):
                    for l in range(0, len(Graph[j])):
                        if Graph[i][k] == Graph[j][l]:
                            continue
                        if Graph[i][k] in Graph[j] or Graph[j][l] in Graph[i]:
                            continue
                        if random.randint(0, 100) < percentage:
                            temp = Graph[i][k]
                            Graph[i][k] = Graph[j][l]
                            Graph[j][l] = temp
                        #print i, j, Graph[i][k], Graph[j][l] 

    return Graph

def Add(Graph, possibility):
    count = {}
    for i in range(1, Graph['level']):
        count[i] = 0

    No = 0
    for level in range(0, Graph['level'] - 1):
        for point in Graph['level%d' %level]:
            count[1] += len(Graph[point])

    for level in range(0, Graph['level'] - 1):
        for hunter in Graph['level%d' %level]:
            for preyLevel in range(level + 2, Graph['level']):
                for prey in Graph['level%d' %preyLevel]:
                    if random.randint(0, 100000) < (possibility / 100.0) ** (preyLevel - level) * 100 * 1000:
                        Graph[hunter].append(prey)
                        count[preyLevel - level] += 1
    print "Number of the relationship cross levels according to the levels it crosses\n", count
    return Graph

def Cycle(level, num):
    return level * 500, num * 500, level * 500 + 100, num * 500 + 100

def ImageOutput(Graph, path):
    Width = 0
    for level in range(0, Graph['level']):
        Width = max(Width, len(Graph['level%d' %level]))
    Width *= 500 + 200
    Height = Graph['level'] * 500 + 200
    co = {}
    image = Image.new('RGB', (Width, Height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    for level in range(0, Graph['level']):
        num = 0
        for points in Graph['level%d' %level]:
            num += 1
            draw.ellipse(Cycle(num, level), fill = (127, 127, 127))
            co[points] = Cycle(num, level)
    for level in range(0, Graph['level']):
        for i in Graph['level%d' %level]:
            for j in Graph[i]:
                if j in Graph['level%d' %(level + 1)]:
                    draw.line((co[i][0] + 50, co[i][1] + 50 , co[j][0] + 50, co[j][1] + 50), fill = (127, 0, 0), width = 5)
                else:
                    draw.line((co[i][0] + 50, co[i][1] + 50 , co[j][0] + 50, co[j][1] + 50), fill = (0, 0, 0), width = 10)

#    image.save('output.jpg', 'jpeg')
    image.save(path, 'jpeg')

    print Graph
    return Graph

def FileOutput(Graph, path):
    output = open(path, 'wb')
    for item in Graph.items():
        output.write("%r\n%r\n%r\n%r\n" %(type(item[0]), type(item[1]), item[0], item[1]))

    return Graph

def Match(GraphA, GraphB):
    AMatch = []
    BMatch = []

    GraphA['level-1'] = []
    GraphB['level-1'] = []
    tmpA = GraphA['level%d' % GraphA['level']]
    tmpB = GraphB['level%d' % GraphB['level']]
    GraphA['level%d' % GraphA['level']] = []
    GraphB['level%d' % GraphB['level']] = []

    for level in range(0, GraphA['level']):
        if level >= GraphB['level']:
            break
        tmp_list = []
        tmp_list += GraphB['level%d' %(level - 1)]
        if (level + 1 < GraphB['level']):
            tmp_list += GraphB['level%d' %(level + 1)]

        for point in GraphA['level%d' %level]:
            AMatch.append(tmp_list)

    for level in range(GraphB['level']):
        if level >= GraphA['level']:
            break
        tmp_list = []
        tmp_list += GraphA['level%d' %(level - 1)]
        if (level + 1 < GraphA['level']):
            tmp_list += GraphA['level%d' %(level + 1)]

        for point in GraphB['level%d' %level]:
            BMatch.append(tmp_list)

    Match = (AMatch, BMatch)

    return Match

def FOutputMatch(Match, path):
    output = open(path, 'wb')
    for result in Match:
        for i in range(0, len(result)):
            output.write('{%d :' %i)
            for value in result[i]:
                output.write(' %d' %value)

            output.write('}\n')

        output.write('\n')

    return Match

def MatchToPair(Match):
    Pair = []
    for result in Match:
        for predator in range(0, len(result)):
            for prey in result[predator]:
                Pair.append((predator, prey))
 
    print "Pair:"
    print Pair
    return Pair

def PairCmp(A, B):
    if (A[0] - B[0]):
        return A[0] - B[0]
    return A[1] - B[1]

#def Pick(Pair, PossibilityFunction):
#    index = random.sample(range(0, len(Pair)), PossibilityFunction(len(Pair)))
def Pick(Match, PossibilityFunction):
    Possibility = PossibilityFunction(len(Match[0]))
    index = random.sample(range(0, len(Match[0])), Possibility)
    index.sort()
    print "index:\n", index
    print "Match:\n", Match
    Relation = []
    for i in index:
#        Relation.append(Pair[i])
        Relation.append((i, Match[0][i][random.randint(0, len(Match[0][i]))]))

    print "Relation:"
    print Relation
    return Relation

def FOutputPick(Relation, Path):
    output = open(Path, 'wb')
    for item in Relation:
        output.write('%d %d\n' %(item[0], item[1]))
    
    return Relation

PickingPossibilityFunction = (lambda(x): int(float(raw_input("Picking possibility(%):\n") / 100 * x)))

def NoProcessOutput(Graph1, Graph2):
    return Pick(Match(Graph1, Graph2), PickingPossibilityFunction), 

def Default(Graph1, Graph2):
    return (FOutputPick(Pick(FOutputMatch(Match(Graph1, Graph2), 'Match.Output.txt'),
        (PickingPossibilityFunction)), "Relation.out"))

def main():
    return\
        FOutputPick(Pick(FOutputMatch(Match(FileOutput(ImageOutput(Add(RandSwap(Generate(Read()),
            float(raw_input("Percentage(%)\n"))), float(raw_input('Base(%)\n'))), 'output1.jpg'), 'Graph1.txt'),
            FileOutput(ImageOutput(Add(RandSwap(Generate(Read()), float(raw_input("Percentage(%)\n"))), 
            float(raw_input('Base(%)\n'))), 'output2.jpg'), 'Graph2.txt')), 'output.txt'),
            (PickingPossibilityFunction)), "Relation.out")

#--main--

if __name__ == '__main__':
    main()

