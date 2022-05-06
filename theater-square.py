import math

def foo():
    bar = input()
    list = bar.split()
    n = int(list[0])
    m = int(list[1])
    a = int(list[2])
    
    i = math.ceil(n/a)
    if a < m:
        i *= math.ceil(m/a)

    print(i)

foo()