

from PIL import Image
from PIL import ImageDraw
import random
import re

def Read():
    List = []
    for num in re.sub(r'[ ]+', ' ', raw_input()).split(' '):
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
        begin = Graph['level%d' %level][0]
        next = Graph['level%d' %(level + 1)][0]
        maximum = Graph['level%d' %(level + 1)][-1]
        for point in Graph['level%d' %level]:
            Graph[point] = range(next + point - begin, min((next + point - begin + 3), maximum) + 1)

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
    for i in range(0, Graph['level']):
        count[i] = 0
    for level in range(0, Graph['level']):
        for hunter in Graph['level%d' %level]:
            for preyLevel in range(level + 2, Graph['level'] + 1):
                for prey in Graph['level%d' %preyLevel]:
                    if random.randint(0, 100000) < possibility ** (preyLevel - level) * 1000:
                        Graph[hunter].append(prey)
                        count[preyLevel - level] += 1
    print count
    return Graph

def Cycle(level, num):
    return level * 500, num * 500, level * 500 + 100, num * 500 + 100

def Output(Graph):
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
                    draw.line((co[i][0] + 50, co[i][1] + 50 , co[j][0] + 50, co[j][1] + 50), fill = (127, 40, 40), width = 10)
                else:
                    draw.line((co[i][0] + 50, co[i][1] + 50 , co[j][0] + 50, co[j][1] + 50), fill = (0, 0, 0), width = 10)

    image.save('output.jpg', 'jpeg')
    #print Graph
        
#--main--
k = float(raw_input('Base\n'))
Output(Add(RandSwap(Generate(Read()), float(raw_input("Percentage"))), (k)))
