'''
Dictionary - Count the occurance of names given a list
and creates a Dictionary.

'''

def frequency(names):
    counters = {} # empty dictionary

    for name in names:  # loops through list of names
        if name in counters: # if the name exists
            counters[name] += 1 # adds counts the name

        else:
            counters[name] = 1 # put the name in the counters dictionary

    return counters

names = ['Bill', 'Sue', 'Joe', 'Sue', 'Debbie', 'Bill']
print(frequency(names))
