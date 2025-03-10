
Text = "lorem ipsum dolor sit amet, consectetur adip"
words = Text.split()
def checker(i,w):
    if w[i] == "dolor":
        checker(i,+1,w)  # check again with new indexes
    else:
        return True

print(checker(0, words))    
    