# except one parameter/string and get rid of punctuation

def removepunct(str1):
    table = str.maketrans(",.?!@#$%^&*()", "$$$$$$$$$$$$$")
    str1 = str1.translate(table)
    str1 = str1.replace('$', '')
    return str1

print(removepunct("This! should,,,,,, ....work$*^^^^, yes???"))
