def perm(x, index=0):
    if index == len(x) - 1:
        print(''.join(x))
        return
    for i in range(index, len(x)):
        x[index], x[i] = x[i], x[index]
        perm(x, index + 1)
        x[index], x[i] = x[i], x[index]

x = list(input())

perm(x)

