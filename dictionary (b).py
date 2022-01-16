'''
ID-20CS037
NAME-SHREYAN MITTAL
AIM-
b.Write a Python script to merge two Python dictionaries.
'''


d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d2.copy()
d.update(d1)
print(d)
