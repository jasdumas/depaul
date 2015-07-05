def vowels(charString):           
    A = charString.count("a")
    E = charString.count("e")
    I = charString.count("i")
    O = charString.count("o")
    U = charString.count("u")
    return [A, E, I, O, U]

string = 'this is a test to see if my program can accurately count the vowels'

print(vowels(string))


def rvowels(charString):
    if not charString:
        return 0
    return (1 if charString[0] in 'aeiouAEIOU' else 0) + rvowels(charString[1:])


print(rvowels(string))

################################ time tests
import time

beg = time.time()

for i in range(100):

    print(rvowels("this is a test to see if my program can accurately count the vowels"))
    #print(vowels("this is a test to see if my program can accurately count the vowels"))

end = time.time()

print("Elapsed time for recursive method: ", end-beg)

