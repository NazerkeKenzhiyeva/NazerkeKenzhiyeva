def sqr(n):
    for i in range(n+1):
        yield i**2

n = int(input())

generator = sqr(n)
for s in generator:
    print(s)  
