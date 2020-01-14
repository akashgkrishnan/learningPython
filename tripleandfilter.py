def triple_and_filter(l):
    return list(x*3 for x in filter(lambda x: x % 4 == 0,l))

 #   def triple_and_filter(lst):
  #      return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))

print(triple_and_filter([1,2,3,4]))