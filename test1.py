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



def test():
    
    fdg = 0
    tries = 5
    correct = 0
    letter = []
    num = ["1","2","3","4","5","6","7","9","0"]
    
    while True:
        if correct == len(word):
            print("got it")
            break
        
        if tries == 0:
            print("game over")
            break
        
        print("letter or word?")
        _try = str(input(">"))
    
        if _try == "" and fdg > 0:
            tries -=1
            print(f"{tries} tries remaining")

        if _try in letter:
            print("given")
            tries -=1
            print(f"{tries} tries remaining")
        
        
        elif _try in num:
            print("just letter or word.")

        elif len(_try) > 1 and _try != word:
            print("nop")
            tries -= 1
            print(f"{tries} tries remaining")
            
        elif _try == word:
            print("got it")
            break

        elif _try == "":
            print("need charactere")
            fdg += 1
        
        elif _try in word:
            letter.append(_try)
            print(_try,"is correct")
            correct += 1
            for index,x in enumerate(word):
                if _try == x:
                    _help[index] = _try
            print(_help)
        
        else:
            tries -= 1
            print("false")
            print(f"{tries} tries remaining")
test()