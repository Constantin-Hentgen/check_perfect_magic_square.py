array = []
compute = []
temp = 0
perfect = 0
square = int(input('Enter the square size : '))

for a in range(0,square**2):
    array.append(int(input('Fill your array : ')))
    
for b in range(0,square): 
    for c in range(0+square*b,square+square*b):
        temp += array[c]
    compute.append(temp)
    temp = 0
    
for d in range(0,square):
    if d == 0:
        temp += array[0]
    else:
        temp += array[d*square+d]
compute.append(temp)
temp = 0

for e in range(0,square):
    if e == 0:        
        temp += array[square-1]
    else:
        temp += array[square-1+e*(square-1)]
compute.append(temp)
temp = 0

for f in range(0,len(compute)-1):
    if compute[f] == compute[f+1]:
        temp += 1
        if compute[f] <= square**2 and compute[f] >= 1 :
            perfect += 1

if temp == len(compute)-1 and compute[0] == compute[-1]:
    print('You got a magic square :)')
    if perfect == len(compute)-1 and compute[-1] <= square**2 and compute[-1] >= 1:
        print('You even got a perfect magic square OMG')

else:
    print("Your square isn't interesting...")
    
        
