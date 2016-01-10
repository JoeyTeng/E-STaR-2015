import os
import re
import sys
from __main__ import main

def Get():
    input = open('log.tmp')
    string = ''
    for line in input:
        if line[:6] == 'Period':
            string = line
        string = string[string.find('('):string.find(')')]
        period = int(string[string.find('(') + 1, string.find(',')])
        if period > 100:
            return True
    return False

def Generator(content):
    i = [0] * 8
    for i[1] in xrange(10, 100, 10):
        for i[2] in xrange(10, 1000, 10):
            for i[3] in xrange(10, 1000, 10):
                for jtmp in xrange(1, 10):
                    i[4] = ktmp / 10.0
                    for i[5] in xrange(((max(i) + 99)/100) * 100, 5000, 100):
                        for ltmp in xrange(1, 10):
                            i[6] = ltmp / 10.0
                            for mtmp in xrange(1, 10):
                                i[7] = mtmp / 10.0
                                for ntmp in xrange(1, 10):
                                    i[8] = ntmp / 1000.0
                                    result = content[:3]
                                    for a in i:
                                        result.append(str(a) + '\n')
                                    result.append(content[-1]) 
                                    yield result

def Change(path, content, G):
    output = open(path, 'wb')
    t = G.next()
    output.writelines(t)
    output.close()

def run():
    inputpath = sys.argv[1] + '.tmp'
    content = open(sys.argv[1], 'rb').readlines()
    G = Generator(content)
    os.mkdir('result.tmp')
    os.chdir('result.tmp')
    count = 0
    while True:
        count += 1
        os.mkdir(str(count))
        os.chdir(str(count))
        while (not Get()):
            Change(inputpath, content[:], G)
            input = open(inputpath, 'rb')
            sys.stdin = input
            output = open('log.tmp', 'wb')
            sys.stdout = output
            main()
            input.close()
            output.close()

        os.chdir('..')

if __name__ == "__main__":
    run()
