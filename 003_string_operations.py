s1 = 'This is simple sentence' # simple sentence
s2 = 'This is mr. O\'Harry' # Control character
print(s1,'\n' + s2)

# row sentence
print(r'This is cat miss O\'dim')

# Muliline string
print('''This 
is
simple
string
''')

# Nesting the string
name = 'Al'
age = 74
print('Mam na imię %s i mam %s lat' %(name, age))
print(f'Mam na imię {name} i mam {age} lat')

# Method use with string
c1 = 'wisła płock'
print(c1.upper())
c2 = 'Chelsea London'
print(c2.lower())

# start/end swith() method
print(c1.startswith('w'))
print(c2.endswith('n'))

# join and split method
cloubs = ['Wisła_Płock', 'Chelsea_London']
print('@'.join(c1))
print('@'.join(cloubs))

print(c1.split())
print(c2.split(','))

# r/l/center just method
print(c1.rjust(20, '*'))
print(c2.ljust(20, '-'))
print(name.center(20, '-'))
