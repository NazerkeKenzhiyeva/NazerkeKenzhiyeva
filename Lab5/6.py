import re
word = input()

need= re.sub('[ ,.]', ':', word)

print(need)
