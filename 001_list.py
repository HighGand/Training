woman = ['Joanna', 'Aleksandra', 'Wioletta', 'Agnieszka']
man = ['Dariusz', 'Wojciech', 'Kacper', 'Paweł']
# Prints lists names
print(woman, man)

# Prints the name with the list after the index
print(woman[3])

# prints the slice of the list
print(woman[0:10])
print(woman[0:-2])

# Getting the length
print(len(woman))

# Change the value list
woman[3] = 'Karolina'
print(woman)

# Concatenation of the lists
all = woman + man
print(all)

# Delete value of the list
del woman[3]
del man[3]

# Use the for loop on the both lists
for i in woman:
    print(woman)
for j in man:
    print(man)

similar = []
for x in woman:
    for y in man:
        if x == y:
            similar.append(x)
if similar:
    print(similar)
else:
    print('Listy nie mają tych samych imion')

# Assigning
mother, douther, sister = woman
print(douther)

# Use the enumerate function with list
for index, item in enumerate(woman):
    print(index, item)

# Add value for append and insert method
woman.append('Agnieszka')
man.append('Romek')

woman.insert(3, 'Klara')
man.insert(3, 'Marek')
print(woman, man)

# Deleta values with remove method
woman.remove('Klara')
man.remove('Romek')
print(woman, man)

# Sorting with list
woman.sort()
man.sort()
print(woman, man)

# Reverse value
woman.reverse()
man.reverse()
print(woman, man)
