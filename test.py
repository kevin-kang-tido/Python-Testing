
# this day one of python classes

# Array = []

# n = 12; 

def meth(n):
    if n == 0: 
        return 1
    else: 
        return n * meth(n-1)

print(meth(3))


## old code 
Array=[]

def meth(i, Arr):
    var=input("Add a number to the array: ")
    Arr.append(var)
    if(i<10):
        meth(i+1,Arr)

meth(0,Array)
print(Array)


    