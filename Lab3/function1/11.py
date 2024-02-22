def palin(word):
    return word == word[::-1]

word = input()
result = palin(word)
print( result)