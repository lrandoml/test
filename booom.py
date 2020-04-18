#abcdefghijklmnopqrstuvwxyz
a = "abcdefghijklmnopqrstuvwxyz"
z = -1

for i in a:
    print(a.replace(i,"*").replace(a[z],"*").replace(a[0],"*").replace(a[-1],"*"))
    z -= 1

