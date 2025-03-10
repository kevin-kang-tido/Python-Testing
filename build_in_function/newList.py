

listTest = [3,9,21,13,10,8,22,30,60]
print("=========== Using Map =============")
new_list = list(map(lambda x: x / 2 ,listTest))

print(new_list)

s_list = sorted(new_list)
print(s_list)
l_list = sorted(listTest)
print(l_list)

# filter function 

print("=========== Using filter =============")
f_list = list(filter(lambda x:x > 5 ,listTest))
print(f_list)

## using filter to find odd numbers

print("=========== Using filter =============")
o_list = list(filter(lambda x:x % 2 != 0 ,listTest))

print(o_list)