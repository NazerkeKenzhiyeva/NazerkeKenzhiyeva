def uni(l):
    result = []
    for i in l:
        if i not in result:
            result.append(i)
    return result


l =[]
n = int(input())
for x in range(n):
    d= int(input())
    l.append(d)
result = uni(l)
print( result)
