import re

word = input()

matches = re.findall(r'[A-Z][a-z]+', word)

if matches:
    print(matches)
else:
    print("No matches")
