data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
numbers = []
letters = []

for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)
        
numbers.remove(6.13)
numbers.sort()


numbers.remove(True)
letters.append(True)

letters.reverse()
letters = ['t' if l == 'T' else 'c' if l == 'C' else l for l in letters]
letters.clear ()
word = ['p', "U", "B", "G"]
letters.extend(word)

letters = tuple(letters)
numbers = tuple(numbers)
print (letters)
print (numbers)