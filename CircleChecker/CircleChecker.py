from sys import argv

def main(History):
    Dict = {}
    count = 0
    second = []
    period = 0
    for item in History:
        key = tuple(item)
        try:
            Dict[key] += 1
            second = item
            period = count
            break
        except:
            Dict[key] = 1
        count += 1

    return count, second

#--main--

if __name__ == '__main__':
    print "period ", main(open(argv[1], 'rb').readlines())
