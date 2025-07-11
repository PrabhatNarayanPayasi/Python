ep1 = {123:89 , 456:90 , 789:94};
ep2 = {223:87 , 334:86 , 446:84};
# print(ep1.update(ep2));
# ep1.update(ep2);
# ep1.clear();
# ep1.pop(123)
# ep1.popitem();
# del(ep1)
del ep1[123]
print(ep1);               





'''
Dictionary Methods
Dictionary uses several built-in methods for manipulation.They are listed below

update()
The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)
Output:
{'name': 'Karan', 'age': 19, 'eligible': True}
{'name': 'Karan', 'age': 20, 'eligible': True, 'DOB': 2001}
Removing items from dictionary:
There are a few methods that we can use to remove items from dictionary.

clear():
The clear() method removes all the items from the list.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)
Output:
{}
pop():
The pop() method removes the key-value pair whose key is passed as a parameter.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)
Output:
{'name': 'Karan', 'age': 19}
popitem():
The popitem() method removes the last key-value pair from the dictionary.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)
Output:
{'name': 'Karan', 'age': 19, 'eligible': True}
del:
we can also use the del keyword to remove a dictionary item.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)
Output:
{'name': 'Karan', 'eligible': True, 'DOB': 2003}
If key is not provided, then the del keyword will delete the dictionary entirely.

Example:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)
Output:
NameError: name 'info' is not defined'''