def compact(lis):
    return [val for val in lis if val]


print(compact([0,1,2,"",[], False, {}, None, "All done"]))