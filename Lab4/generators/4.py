def sqr(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = int(input())
b = int(input())
        
generator = sqr(a,b)
        
for elem in generator:
    print(elem)