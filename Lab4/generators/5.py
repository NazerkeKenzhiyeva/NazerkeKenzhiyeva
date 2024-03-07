def down(n):
    while n >= 0:
        yield n
        n -= 1


n = int(input())
        
generator = down(n)
        
for elem in generator:
    print(elem)