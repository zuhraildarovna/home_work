my_dict={'Ilya': 1987, 'Victor': 1985,' Marina' : 2000}
print(my_dict)
print(my_dict.get('Ilya'))
print(my_dict.get('Sonya'))
my_dict.update({'Misha': 2001 ,
                'Masha': 1993})
print(my_dict)
a=my_dict.pop('Ilya')
print(a)
print(my_dict)
my_set={1,1,1,5,5,6,4,37}
print(my_set)
my_set={1,2,2,3,5,'string',False}
print(my_set)
print(my_set.discard(3))
print(my_set)