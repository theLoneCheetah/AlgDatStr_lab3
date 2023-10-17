def rascheska(s):
    step = len(s) - 1
    while step > 0:
        for i in range(0, len(s) - step):
            if s[i] > s[i + step]:
                s[i], s[i + step] = s[i + step], s[i]
        step -= 1
    return s


a = [int(i) for i in input().split()]
print(rascheska(a))