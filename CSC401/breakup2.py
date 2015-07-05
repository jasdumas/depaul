## return two lists from one string of names

def breakup2(str1):
    str1 = str1.lower()
    list1 = str1.split()
    wordList1 = []   #intilizing a NULL list
    wordList2 = [] 


    for word in list1:
        if word[0] >= 'a' and word[0] <= 'm':
            wordList1.append(word) # adds word to the list
        else:
            wordList2.append(word)

    return [wordList1, wordList2] # you can only return 1 item and to trick it you can put it in on list w/ a bracket
print(breakup2('this is a test string to see'))
            
