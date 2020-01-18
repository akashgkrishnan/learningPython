D = {'A': 'APple', 'e101': 'Akash', 'chris': '10', 1.5 : 1000}
print(D)
D['e101'] = 'new'
D['CA'] = 78
print(D)


del D[1.5]
print(D)


print(D['A']) # if the key is in the dictionay then will return the  value else it will throw error

print(D.get('A','not found')) 
print(D.get('B','not found')) 
