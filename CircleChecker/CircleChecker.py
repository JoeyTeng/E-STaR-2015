from sys import argv

def main(History):
    Dict = {}
    count = 0
    second = []
    period = 0
    next = []
    for item in History:
        key = tuple(item)
        try:
            Dict[key] += 1
            second = item
            break
        except:
            Dict[key] = 1
        count += 1
        
    next.append(count)
    while period == 0:
        count += 1
        for item in History[count:]:
            if item == second:
                next.append(count)
                break
            count += 1
        if len(next) > 2:
            for i in range(len(next) - 1, 2, -1):
                if next[i] + next[i - 2] == 2*next[i - 1]:
                    period = next[i] - next[i - 1]

    return period, next, count, second

#--main--

if __name__ == '__main__':
    print "period ", main(open(argv[1], 'rb').readlines())
