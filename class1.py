# Package should contain simillar modules + sub packges
# management of modules becomes easy 
# Advantages of package 
# easy management of modules
# solve the problem of naming conflict between modules 

# import  folder_name
# import  folder_name.file_name.function_name as alias_name
# import  folder_name.sub_folder.file_name.function_name
# from folder_name import module_name
# from folder_name import module_name as alias_name
# from folder_name.module_name  import function_name1, function_name 2



from ducat.arith import add
from ducat.arith2 import diff
from ducat.arith3 import algebra


print(add(1,8))
print()