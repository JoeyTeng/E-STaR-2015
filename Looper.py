import os
import re
import sys
from callable import *

Flag = True
def Get():
    try:
        input = open('log.tmp', 'rb')
    except IOError:
        return False
    string = ''
    for line in input:
        if line[:6] == 'Period':
            string = line
            print string
            print string.find('(') + 1
            print string.find(',')
            period = int(string[string.find('(') + 1: string.find(',')])
            if period > 100:
                return True
    return False

def Generator(content):
    i = [0] * 9
    for i[0] in xrange(10, 100, 10):
        for i[1] in xrange(10, 1000, 10):
            for i[2] in xrange(10, 1000, 10):
                for jtmp in xrange(1, 10):
                    i[3] = jtmp / 10.0
                    for i[4] in xrange(((max(i) + 99)/100) * 100, 5000, 100):
                        for ltmp in xrange(1, 10):
                            i[5] = ltmp / 10.0
                            for mtmp in xrange(1, 10):
                                i[6] = mtmp / 10.0
                                for n1tmp in xrange(1, 10):
                                    i[7] = n1tmp / 1000.0
                                    for n2tmp in xrange(1, 10):
                                        i[8] = n2tmp / 1000.0
                                        result = content[:3]
                                        for a in i:
                                            result.append(str(a) + '\n')
                                        result.append(content[-2])
                                        result.append(content[-1])
                                        print result
                                        yield result
    Flag = False

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
    while Flag:
        count += 1
        os.mkdir(str(count))
        os.chdir(str(count))
        while (not Get()):
            Change(inputpath, content[:], G)
            print "start"
            tmpin = sys.stdin
            input = open(inputpath, 'rb')
            sys.stdin = input
            tmpout = sys.stdout
            output = open('log.tmp', 'wb')
            sys.stdout = output
            main()
            sys.stdin = tmpin
            sys.stdout = tmpout
            print "DONE"
            input.close()
            output.close()

        os.chdir('..')

if __name__ == "__main__":
    run()
