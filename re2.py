import re
def parse_bytes(binary):
    pattern = re.compile(r'\b[0-1]{8}\b')
    return pattern.findall(binary)



print(parse_bytes('11011101 is my 11001101'))