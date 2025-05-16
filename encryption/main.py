import random

Array = [0,1,2,3,4,5]

for i in range (len(Array)):

    rnd = random.randint(0,5)
    
    Value = Array[i]

    Array[i] = Array[rnd]

    Array[rnd] = Value

print(Array)
