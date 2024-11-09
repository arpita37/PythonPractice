my_list = [1,2,3]
my_list = [1,"abjgs", 10.4233,(1,2,)]
print(len(my_list))
print(my_list)

## string is mutable
my_list[0] = 100
print(my_list)

my_list.append(6) ##3in place
print(my_list)
my_list.pop()
my_list = [1,4,2,4,2]
print(my_list)
my_list.sort() ##inplace
print(my_list)
val = my_list.sort() ## returns None
print(val)