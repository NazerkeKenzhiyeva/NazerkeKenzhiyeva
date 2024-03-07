import re

word = input()

snake_string = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', word).lower()

print(snake_string)

