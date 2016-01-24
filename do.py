from sys import argv
import os

start, end = input("Start, end")
no = input("No")

f = open(argv[1], 'rb').readlines()
for i in xrange(start, end):
    open('t.m.p', 'wn').writelines(f[:3] + ['%d\n' %i] + f[4:])
    os.system('python __main__.py <t.m.p')
    os.rename('./data.csv', '/Users/Toujour/Desktop/data.1.%d.2.%d.csv' %(i, no))
