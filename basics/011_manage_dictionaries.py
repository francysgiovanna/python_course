Dictionary = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(Dictionary)
print(Dictionary['food'])
Dictionary ['quantity'] = 10
print(Dictionary)
Dictionary ['quantity'] = Dictionary ['quantity'] + 15
print(Dictionary)
Dictionary ['quantity'] += 15
print(Dictionary)
dict_complex = {'name': {'first': 'Bob', 'last': 'Smith'},'job': ['dev', 'mgr'],'age': 40.5}
print(dict_complex)
print(dict_complex['name'])
print(dict_complex['name']['first'])
dict_complex['job'].append('admin')
dict_complex['age'] = 15
dict_complex['name']['first'] = 'Francys'
dict_complex['name']['last'] = 'Higuera'
print(dict_complex)
list_keys = list(dict_complex.keys())
print(list_keys)
print(list_keys.sort())
dict_complex['name']['first'] = dict_complex['name']['first'].upper()
dict_complex['name']['last'] = dict_complex['name']['last'].upper()
for key in list_keys: 
    print(key,' --- ',dict_complex[key])
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)
squares = []
items = [2,4,6,8]
for item in items:
    squares.append(item**2)
print(squares)
Dictionary ['food'] = 'bread'
print(Dictionary)
Dictionary ['quantity'] = 18
print(Dictionary)
Dictionary ['color'] = 'blue'
print(Dictionary)
dict_complex['age'] = 48
dict_complex['name']['first'] = 'Javier'
dict_complex['name']['last'] = 'Gonzalez'
print(dict_complex)
