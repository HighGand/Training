myCat = {'size': 'gruby', 'color': 'szary', 'disposition': 'głośny'}
print(myCat)
# keys, values, items method
print(myCat.keys())
for k in myCat.keys():
    print(k)

print(myCat.values())
for v in myCat.values():
    print(v)

print(myCat.items())
for k, v in myCat.items():
    print(k, v)

# get method
picnicItems = {'apples': 5, 'cups': 3}
print('Kubki', picnicItems.get('cups', 0))
print('Jajka', picnicItems.get('eggs', 0))

# setdefoult method
myCat.setdefault('wiek', 6)
print(myCat)
