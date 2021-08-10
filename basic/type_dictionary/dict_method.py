data = dict()

data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'

# only keys
key_list = data.keys()

# only values
value_list = data.values()

print(key_list)
print(value_list)

# print each elements by key in the type_dictionary
for key in key_list:
    print(data[key])
