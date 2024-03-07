def div3and4(n):
    for i in range( n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


n = int(input())
        
generator = div3and4(n)
        
for elem in generator:
    print(elem)
