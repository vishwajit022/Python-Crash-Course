import random
import p5_something

random_int =random.randint(1,10)
print(random_int)

#Accessing a different file 
print(p5_something.s)

random_float=random.random()
print(random_float)

#Using Heads and tails
coin_face=random.randint(0,1)
if coin_face ==1:
    print("Heads")
else:
    print("Tails")