countOfWords=int(input("enter total words to enter: "))
listOfWords=[]
for word in range(countOfWords):
    listOfWords.append(input("enter word here:"))

print("entered words are",listOfWords)
# sort_list   = quicksort(listOfWords)
sorted(listOfWords,key=str.lower,reverse = True)
print(listOfWords)

for x in listOfWords:
    print (x)

# Output
# enter total words to enter: 3
# enter word here:zxcv
# enter word here:asdf
# enter word here:oiuy
# entered words are ['zxcv', 'asdf', 'oiuy']
# ['zxcv', 'asdf', 'oiuy']