import re

word = input()

matches = re.findall("[a-zA-Z]+_[a-zA-Z]+", word)

if matches:
    print(matches)
else:
    print("No matches")



