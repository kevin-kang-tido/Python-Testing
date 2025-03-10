
list = [2, 3, 4, 5, 6, 7, 8, 9]

def power(myfun,list):
    # create a new list to shore a new valuse 
    new_list = []
    for i in range(len(list)):
        # create varible to data 
        new_var = myfun(list[i])
        # add data to new list
        new_list.append(new_var)
    return new_list

print(power(lambda x:x*x,list))