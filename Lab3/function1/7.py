def has_33(listt):
    for i in range(len(listt) - 1):
        if listt[i] == 3 and listt[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))     
print(has_33([1, 3, 1, 3]))  
print(has_33([3, 1, 3]))      
