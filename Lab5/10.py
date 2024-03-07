import re

rule1 = re.compile(r'ab*')
strings1 = ["a", "abc", "abbc", "abbb"]

for test in strings1:
    if rule1.fullmatch(test):
        print(test, "matches the rule")
    else:
        print(test, "doesn't match the rule")