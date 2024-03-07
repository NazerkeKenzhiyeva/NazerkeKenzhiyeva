import re

word = input()
need = re.match(r"^ab*$", word)

if need:
    print("YES! We have a match!")
else:
    print("No match")

