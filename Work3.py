import random

password = ["+","-","/","?","#","%","a","b","c","d","e","f","g","A","B","C","D","E","F","G","=","*","1","2","3","4","5","6","7","8","9","0"]

b = int(input("şifrenin uzunluğunu yazın."))

d = []

for i in range(b):
    c = random.choice(password)

    d.append(c)

print(d)


