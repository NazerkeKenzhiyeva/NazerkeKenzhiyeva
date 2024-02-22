l =[]
n = int(input())
for x in range(n):
    d= int(input())
    l.append(d)

prime = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1, l))

print(prime)

