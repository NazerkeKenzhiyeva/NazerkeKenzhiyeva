import re

word = input()
need = re.match(r"^a(bb|bbb)$", word)

if need:
    print("YES! We have a match!")
else:
    print("No match")
