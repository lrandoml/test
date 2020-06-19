
from random_word import RandomWords
from random import choice

#random_word lib required

r = RandomWords()
word = r.get_random_word()


_help = []
for i in word:
    i = "*"
    _help.append(i)

tries = 7
print(*_help)

print(f"U have {tries} tries.")



def test(tries):

    fdg = 0
    correct = 0
    letter = []
    num = ["1","2","3","4","5","6","7","9","0"]
    
    while correct != len(word):
        
        if tries == 0:
            print(f"the word was : {word} \ngame over")
            break
        
        print("\nletter or word?\n")
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
            for index,x in enumerate(word):
                if _try == x:
                    correct += 1
                    _help[index] = _try
                    
            print(*_help)
        
        else:
            tries -= 1
            print("\nfalse")
            print(f"{tries} tries remaining")
test(tries)
