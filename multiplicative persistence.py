import csv
import keyboard
highest = 0

with open('multiplicative_persistence.csv', 'w', newline='') as csvfile:
    starter = csv.writer(csvfile, delimiter=',',dialect = 'excel',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    starter.writerow([0,0,0])


def analyze(n):
    convert = str(n)
    returnlist = []
    returnlist.append(n)
    while len(str(convert)) != 1:
        digits = [int(i) for i in convert]
        temp = 1
        for j in digits:
            temp*=j
        convert = str(temp)
        returnlist.append(convert)
    return returnlist
        

def updt(newline):
    with open('multiplicative_persistence.csv', 'a', newline='') as csvfile:
        updater = csv.writer(csvfile, delimiter=',',dialect = 'excel',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        updater.writerow(newline)

testvalue = 0
while True:
    testvalue += 1
    valuebreakdown = analyze(testvalue)
    if len(valuebreakdown) > highest:
        print("lowest value with persistence "+str(highest)+" is "+str(testvalue))
        highest+=1
    updt([testvalue, len(valuebreakdown)-1,*valuebreakdown])
    if keyboard.is_pressed('enter'):
        print('stopped on value '+str(testvalue))
        break
