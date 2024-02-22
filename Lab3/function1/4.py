def filter_prime(numbers):
    prime = []
    for x in numbers:
        count = 0
        for i in range(1,x+1):
            if x%i==0:
                count+=1
        if count==2:
            prime.append(x)
    return prime


        
        
        
numbers0 = input()
numbers = list(map(int, numbers0.split()))
print(filter_prime(numbers))

