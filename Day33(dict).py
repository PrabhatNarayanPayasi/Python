dict = {
#   1:{
#       "name":"Prabhat",
#        "class":"B.tech",
#   }
"a":12,
"b":14,
}
print(dict);
print(dict.keys());
print(dict.values())
for i in dict.keys():
    print(f" The value corrosponding to the key are {dict[i]}")
print(dict.items())







'''

Python Dictionaries  
Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
Output:
{'name': 'Karan', 'age': 19, 'eligible': True}
Accessing Dictionary items:
I. Accessing single values:
Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))
Output:
Karan
True
II. Accessing multiple values:
We can print all the values in the dictionary using values() method.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())
Output:
dict_values(['Karan', 19, True])
III. Accessing keys:
We can print all the keys in the dictionary using keys() method.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())
Output:
dict_keys(['name', 'age', 'eligible'])
IV. Accessing key-value pairs:
We can print all the key-value pairs in the dictionary using items() method.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())
Output:
dict_items([('name', 'Karan'), ('age', 19), ('eligible', True)])'''