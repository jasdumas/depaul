def indexfun(filename, wordlist):
    infile = open(filename, 'r')
    content = infile.readlines()                           
    infile.close()              
    emptyDict = {}                       # creates our empty dictionary 
    emptylist = []                       # empty list to store filename lines
    length = len(content)                # 11 lines

    for line in content:                 # splits original file line and adds to emptylist
        b = line.split()
        length1 = len(b)
        emptylist.append(b)
        length2 = len(emptylist)
                            
    for i in range(length):             # line index numbers
        for word in range(len(emptylist[i])):   # for each word of the filename           
            if emptylist[i][word] in wordlist:
                emptyDict[emptylist[i][word]] = i

    for item in emptyDict:
        print(item, " ...... ", emptyDict[item])
            
a = ['network', 'devices', 'computer', 'fire', 'local', 'area','room', 'single']       
   

print(indexfun('Network.txt', a))
