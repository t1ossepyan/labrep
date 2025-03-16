import json
import math
import re
import datetime

def match(s):
    return re.fullmatch(r'ab*', s)

print(match("abbbb"))
