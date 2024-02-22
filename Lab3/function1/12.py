def histogram(l):
    for q in l:
        lisy = []
        for i in range(q):
            lisy.append('*')
        print(' '.join(lisy))
l =[]
n = int(input())
for x in range(n):
    d= int(input())
    l.append(d)
histogram(l)