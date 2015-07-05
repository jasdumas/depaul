def indexfun(filename, wordlist):
    infile = open(filename, 'r')
    content = infile.readlines()                           
    infile.close()                 
    print(content)

    emptyDict = {}                       
    counter = 1
           
    for line in content:
        counter += 1                                       
        b = line.split()
        length1 = len(b)

               
    for word in line:              
        if word in emptyDict[word]:
            emptyDict[word].append(counter)
        else:
            emptyDict[word] = [counter]

    for item in emptyDict:
        print(item, " ...... ", emptyDict[item], )
            
a = ['network', 'devices', 'computer', 'fire', 'local', 'area','room', 'single']       
   

print(indexfun('Network.txt', a))
