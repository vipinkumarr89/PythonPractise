inputValue=input("enter alphanumeric string: ")
digitCounter=0
stringCounter=0
lis=[x for x in inputValue]
for x in lis:
    if x.isdigit():
        digitCounter+=1
    else:
        stringCounter+=1

print("LETTERS: ",stringCounter)
print("DIGITS: ",digitCounter)
