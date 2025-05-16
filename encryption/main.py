import random

Array = [0,1,2,3,4,5]  

for i in range (len(Array)):

    rnd = random.randint(0,5)
    
    Value = Array[i]

    Array[i] = Array[rnd]

    Array[rnd] = Value

print(Array)


NewArray = [1,2,3,4,5,6,7,8,9]

for i in range(len(NewArray)):
  # random 
  ramddomNumer = random.randint(0,9)

  old = NewArray[i]

  NewArray[i] = NewArray[ramddomNumer]

  NewArray[ramddomNumer] = old

print(NewArray)
