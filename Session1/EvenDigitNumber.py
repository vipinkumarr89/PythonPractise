listOfOnlyEvenInTheNumber=[]
for numb in range(1000,3000):
    # print("processing for numb",numb)
    if ((int(numb / 1000) % 2) == 0) and ((int(numb / 100) % 2) == 0) and ((int(numb / 10) % 2) == 0) and ((int(numb / 1) % 2) == 0):
        print(numb)