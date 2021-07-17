myList = [1, 2, 3, 4, 5]

def times2(x):
    return x*2

print(list(map(times2, myList)))

l = lambda x : x*2

print(list(map(l, myList)))