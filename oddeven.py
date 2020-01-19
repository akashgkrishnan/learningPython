lists = [1,2,3,4,5,6]
new_list = ['even' if num%2 == 0 else 'odd' for num in lists]
print(new_list)