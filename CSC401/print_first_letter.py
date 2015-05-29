user = input("enter a sentence and you will recieve the first letter of each word: ") # prompts the user
user = user.split() # splits it into a list so that you can grab each word

for words in user: # for loop to go through the list
    print(words[0]) # prints the first letter of each word in the list
    
    
