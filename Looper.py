import os
import re
import sys
import random
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
            period = int(string[string.find('(') + 1: string.find(',')])
            if period > 100:
                return True
    return False

def Generator(content):
    global dictionary
    dictionary = {}
    exponent = [10, 100, 100, 0.1, 100, 0.1, 0.1, 0.001, 0.001]
    signficand = [10, 10, 10, 10, 50, 10, 10, 10, 10]
    i = [0] * len(exponent)
    while True:
        try:
            count = count
        except UnboundLocalError:
            count = 0
        for index in xrange(0, len(i)):
            i[index] = random.randint(1, signficand[index] - 1)
        result = content[:3]
        tmp = 0
        for index in xrange(0, len(i)):
            t = i[index] * exponent[index]
            tmp *= signficand[index]
            tmp += t
        try:
            dictionary[tmp]
            count += 1
            if count > 1000:
                global Flag
                Flag = False
                return
            continue
        except KeyError:
            dictionary[tmp] = True
        for index in xrange(0, len(i)):
            i[index] *= exponent[i]
        for a in i:
            result.append(str(a) + '\n')
        result.append(content[-2])
        result.append(content[-1])
        print result
        count = 0
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
    global Flag
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
        print count

if __name__ == "__main__":
    run()
