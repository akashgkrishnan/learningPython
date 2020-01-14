'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''

def extract_full_name(full):
    return list(f"{x['first']} {x['last']}" for x in full)
    
    #def extract_full_name(l):
       # return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))

print(extract_full_name([{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]))