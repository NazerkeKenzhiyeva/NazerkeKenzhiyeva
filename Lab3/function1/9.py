def volume(rad):
    pi = 3.14159
    volume = (4/3) * pi * rad**3
    return volume


rad = float(input())
result = volume(rad)
print(result)
