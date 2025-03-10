
# number = 12 

def fatorial(i,n):
    # calculate fatorial 
    if i > n:
        return 1
    else:
        return i * fatorial(i + 1, n)
print(fatorial(1,4))

# 4 * 3 * 2 * 1 = 24