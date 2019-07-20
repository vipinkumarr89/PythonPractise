#1 print length using set
nums =set([1,1,2,3,3,3,4,4])
print(len(nums))

# Output1
#4
## set this print only unique values


#2 print keys
d ={"john":40, "peter":45}
print(list(d.keys()))

# Output2
#['john', 'peter']

#3 A website requires a user to input username and password to register.
#Write a program to check the validity of password given by user.
print("Enter Password here")
import re
regex = re.compile('[$#@a-zA-Z0-9]')
passwd=input("Enter Password here: ")
if len(passwd) >= 6 and len(passwd) <= 12:
    if regex.search(passwd) != None:
        print("Strong Password")

else:
    print("Week password")

#Output3
#Enter Password here: Edureka123@
#Strong Password

#4for loop to print digit and its position
a = [4,7,3,2,5,9]
b=list(zip(a,list(map( lambda x: a.index(x) ,a))))
print (b)

#Output4
#[(4, 0), (7, 1), (3, 2), (2, 3), (5, 4), (9, 5)]

#5 accept alphanumeric string and print even indexed char

def evenAndNotDigit():
    a = input("enter alnum string: ")  # eg. H1e2l3l4o5w6o7r8l9d
    out=''
    for each in a:
        if a.index(each) % 2 == 0 and each.isdigit() != True:
            out+=each

    print("out>>",out)

evenAndNotDigit()


#Output
#enter alnum string: H1e2l3l4o5w6o7r8l9d
#out>> Helloworld

#6 print in reverse order
str=input("Enter string here to reverse: ")
stringlength=len(str)
slicedString=str[stringlength::-1]
print (slicedString)

#Output
#Enter string here to reverse: H1e2l3l4o5w6o7r8l9d
#d9l8r7o6w5o4l3l2e1H

#7 program to count and print the numbers
from collections import Counter
a=input("enter string: ") #e.g., abcdefgabc
mydict=Counter(a)
for letter, count in mydict.most_common(len(mydict)):
    print('%s: %d' % (letter, count))

#Ouptut
# enter string: abcdefgabc
# a: 2
# b: 2
# c: 2
# d: 1
# e: 1
# f: 1
# g: 1

#8 Find common from lists
list1=[1,3,6,78,35,55]
list2=[12,24,35,24,88,120,155]
list3=[]
for each in list1:
    for each2 in list2:
        if int(each) == int(each2):
            list3.append(each)

print(list3)

#Output
#[35]

#9 Remove duplicate and maintain order of list [12,24,35,24,88,120,155,88,120,155]
list1=[12,24,35,24,88,120,155,88,120,155]
mylist=[]
for each in list1:
    mylist.append(each)
mylist = list(dict.fromkeys(mylist))
print(mylist)

#10.By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
list1=[12,24,35,24,88,120,155]
for each in list1:
    if each == 24:
        list1.remove(each)
print(list1)
#[12, 24, 35, 88, 120, 155]
#[12, 35, 88, 120, 155]

#11.By using list comprehension,
# please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
list5=[12,24,35,24,88,120,155]
list6=[0,4,5]

print("before delete",list5)
for each in (reversed(list6)):
    del list5[each]

print("After delete:",list5)

#Ouptut
#before delete [12, 24, 35, 24, 88, 120, 155]
#After delete: [24, 35, 24, 155]

#12.By using list comprehension,
# please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155]
list7=[12,24,35,70,88,120,155]
list8=[]
for each in list7:
    if each % 5 == 0 and each % 7 == 0:
        list8.append(each)
print(list8)

#Output
#[35, 70]

#13.Please write  a  program  to  randomly  generate  a  list  with  5  numbers,
# which  are divisible by 5 and 7 , between 1 and 1000 inclusive
import random
list9=[]
list10=[]
counter=5
print("random number")

for each in range(1,1000):
    # print("each",each)
    # print("randomNumber",randomNumber)
    if each % 5 == 0 and each % 7 == 0:
        list9.append(each)

while(counter >=1):
    list10.append(random.choice(list9))
    counter=counter-1

print(list10)

#Output
#random number
#[385, 350, 525, 385, 140]

#14.Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0).
n=int(input("Enter Sn to find the sum: "))
sum=0
for each in range(5):
    sum=sum+((1+each)/(2+each))

print(sum)

#Output
#Enter Sn to find the sum: 5
#3.5500000000000003















