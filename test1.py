#first try

from random import choice

list_word = ["yes","man","woman","keyboard","mouse","phone"]
word = choice(list_word)

_help = []
for i in word:
    i = "*"
    _help.append(i)

print(_help)
print("U have 5 tries.")
tries = 5
correct = 0

while True:
    if correct == len(word):
        print("got it")
        break
    
    if tries == 0:
        print("game over")
        break
    
    print("letter or word?")
    _try = input(">")
    
    if _try == word:
        print("got it")
        break
    
    elif _try in word:
        print(_try,"is correct")
        correct += 1
    
    else:
        tries -= 1
        print("false")
        print(f"{tries} tries remaining")      

