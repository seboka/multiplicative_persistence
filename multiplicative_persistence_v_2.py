import json
import keyboard
count = 0
beefy = ""
filename = 'much_more_efficient_multiplicative_persistence.json'

with open(filename, 'r') as infile:
    beefy = infile.read()
    previous = json.loads(beefy)
    count = len(previous)
    beefy = beefy[1:len(beefy)-1]+", "

with open(filename, 'w') as outfile:
    outfile.write("["+beefy)

while 1:
    if count%1000==0:
        print(count)
    temp=1
    for i in str(count):
        temp*=int(i)
    count+=1
        
    if keyboard.is_pressed('enter'):
        print('stopped on value '+str(count))
        with open(filename, 'a') as outfile:
            outfile.write(str(temp)+"]")
        break
    else:
        with open(filename, 'a') as outfile:
            outfile.write(str(temp)+", ")
