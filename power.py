
list = [2,3,4,5,6,7]

def power(myfun,lst):
    n_l  = []
    for i in range(len(lst)):
        # Add function valuse 
        new_var = myfun(list[i])
        # ADD to list 
        n_l.append(new_var)
    return n_l

## x = x*x is my function
print(power(lambda x:x*x,list))