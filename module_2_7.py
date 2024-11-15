def print_params(a=1,b='stroka',c=True):
    print(a,b,c)
print_params([3.4,77],False,'govno')
values_list= ['drugaya stroka',False, 77]
values_dict= {'a':7,'b':'toje storka','c':7.7}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['slishkom legko',999]
print_params(*values_list_2,42)