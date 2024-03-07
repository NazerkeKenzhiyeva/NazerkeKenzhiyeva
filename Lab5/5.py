import re

word = input()

match = re.match("^a.*b$", word)

if match:
    print("YES! We have a match!")
else:
    print("No match")
