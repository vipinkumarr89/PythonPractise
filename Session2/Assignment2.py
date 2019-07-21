import re

list2 = []
regex = re.compile('[$#@a-zA-Z0-9]')


def validate(referenceId):
    if len(referenceId) == 12:
        return True

def encrypt(referenceId):
    list1 = list(referenceId)
    if regex.search(referenceId) != None:
        for each in list1:
            list2.append(ord(each)+2)
    return list2

def decrypt(list2):
    str1 = ''
    for each2 in list2:
        str1 = str1 + (chr(each2 - 2))
    return str1

def Main():
    referenceId = input("Enter reference ID here")
    print("Original referenceId")
    print(referenceId)
    if validate(referenceId):
        print("Encrypted ReferenceID")
        list3 = encrypt(referenceId)
        print(list3)

    decyptReferenceID=input("type True or False to decrypt referenceID")
    if decyptReferenceID == True:
        print("Unencrypted ReferenceID")
        str2 = decrypt(list2)
        print(str2)

Main()
''' 
ReferenceID e.g., qazwsxedc12#
'''


