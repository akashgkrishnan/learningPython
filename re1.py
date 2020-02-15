import re


def is_valid_time(times):
    pattern = re.compile(r'^\d{1,2}:\d\d$')
    if pattern.search(times):
        return True
    return False

print(is_valid_time("111:45"))