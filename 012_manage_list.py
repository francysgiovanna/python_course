my_list = [123, 'spam', 1.23, 'francys']
print(my_list)
size = len(my_list)
print(size)
print("first element", my_list[0])
print("third element", my_list[2])
print("last element1", my_list[3])
print("last element2", my_list[size-1])
print("last element3", my_list[-1])
print("prelast element", my_list[-2])
print("first and second element", my_list[0:2])
print("second to third element", my_list[1:3])
other_list = [4, 5, 6]
union = my_list + other_list
print(union)
last_name = ' Higuera'
my_list.append(last_name)
print(my_list)
my_list.pop(3)
print(my_list)
string_list = ['higuera','francys','giovanna','francisco','javier']
string_list.sort()
print(string_list)
string_list.reverse()
print(string_list)