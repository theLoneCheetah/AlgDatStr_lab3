import random

def fast(s):
    if len(s) <= 1:
        return s
    ch = random.choice(s)
    s1 = []
    s2 = []
    s3 = []
    for i in range(len(s)):
        if s[i] < ch:
            s1.append(s[i])
        elif s[i] == ch:
            s2.append(s[i])
        else:
            s3.append(s[i])
    return fast(s1) + s2 + fast(s3)


a = [int(i) for i in input().split()]

print(fast(a))