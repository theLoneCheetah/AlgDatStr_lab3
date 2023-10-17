import timeit

mysetup = ""
mycode = """def rascheska(s):
    step = len(s) - 1
    while step > 0:
        for i in range(0, len(s) - step):
            if s[i] > s[i + step]:
                s[i], s[i + step] = s[i + step], s[i]
        step -= 1
    return s"""
rez = timeit.timeit(stmt=mycode, setup=mysetup, number=1000000)
print(rez * 10 ** 3)