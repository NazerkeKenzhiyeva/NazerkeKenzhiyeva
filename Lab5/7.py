import re

word = input()
camel_case = re.sub(r'_([a-z])', lambda x: x.group(1).upper(), word)
print(camel_case)
