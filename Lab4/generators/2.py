def evenNum(n):
    for i in range(0, n + 1, 2):
        if(i!=0):
             yield i


n = int(input())
        
generator = evenNum(n)
        
for even in generator:
    print(even, end=", "if even < n-1  else "\n")

