name = 'francys giovanna'
size = len(name)
print("name", name)
print("size", size)
print("first ler", name[0])
print("fifth letter", name[4])
print("last letter1", name[15])
print("last letter2", name[size-1])
print("last letter3", name[-1])
print("prelast letter", name[-2])
print("second name", name[8:16])
print("first name", name[0:7])
last_name = ' Higuera'
complete_name = name + last_name
print(complete_name)
prefix = 'miss ' + complete_name
print(prefix)
repition = prefix * 3
print(repition)
find_substring = complete_name.find('ran')
print(find_substring)
find_substring = complete_name.find('wan')
print(find_substring)
replace_substring = complete_name.replace('ran','ren')
print(replace_substring)
capital_letter_string = complete_name.upper()
print(capital_letter_string)
capitalize_string = complete_name.capitalize()
print(capitalize_string)
title_string = complete_name.title()
print(title_string)