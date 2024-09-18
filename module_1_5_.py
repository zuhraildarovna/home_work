immutable_var= 1,2, 's',True
print(immutable_var)
immutable_var=(1,2, 's', True) + (1,2)
print(immutable_var)
immutable_var=(1,2,'s',True) * 2
print(immutable_var)
#immutable_var[0]=10 #изменение невозможно, птому что кортеж хранит ссылку на список, а не сам список
mutable_list=[3,4,'a', True]
print(mutable_list)
mutable_list[0]=9
mutable_list[1]=8
mutable_list[2]='a'
mutable_list[3]=False
print(mutable_list)

