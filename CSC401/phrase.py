phrase = input('Enter a phrase: ')

lst = []
lst2 = []

for c in phrase:
    if c in 'aeiouAEIOU':
        lst.append(c)
for letter in lst:
    if letter in 'aeiouAEIOU':
        lst2.append(lst.count(letter))


print(lst)
print(lst2)
        
        
