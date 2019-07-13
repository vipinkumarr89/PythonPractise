Numb = int(input("Enter the number: "))
listfactor = []
NumbRang=[1,2,3,4]
NumbRang=list(range(1,(Numb+1)))
for i in NumbRang:
    if (Numb % i == 0):
        listfactor.append(i)
    i = i + 1

NumbDict = {}
for x in listfactor:
    if(x %2 == 0):
        NumbDict[x] = "Even"
    else:
        NumbDict[x] = "Odd"

print("Factors for number: ",Numb,"\n")
for dd in NumbDict:
    print(dd, NumbDict[dd])

