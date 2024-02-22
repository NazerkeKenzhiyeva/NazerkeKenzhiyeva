def spy_game(list1):

    pos= 0
    for x in list1:
        if pos == 0 and x == 0:
            pos += 1
        elif pos == 1 and x== 0:
            pos += 1
        elif pos == 2 and x == 7:
            return True

    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5])) 
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0])) 
