import re

def parse_date(date):
    date_group = {}
    pattern = re.compile(r'^(\d\d)[,/.](\d\d)[,/.](\d{4})$')
    result = pattern.search(date)
    if result:
        date_group['d'] = result.group(1)
        date_group['m'] = result.group(2)
        date_group['y'] = result.group(3)
        return date_group
    return None

print(parse_date('29/04/1996'))
print(parse_date('29,04,1996'))
print(parse_date('29.04.1996'))
print(parse_date('29.04.1996222'))