
import random
from random import choice
m = 0


print("Is?")
while m < 6:
    z = [ 2 ,3 , 4 , 5 , 6 , 7 , 8  ,9,11,12,13,14 ]
    v = [2,3,4,5,6,7,8,9,1,11,12,13,14,15,16]

    x = random.choice(z)
    y = random.choice(v)
    
    per_ans = x * y
    question = print(x , "X" ,y, "\n")
    answer = int(input(":"))
    if answer == per_ans:
        print("Too Slow, Get faster \n")
    else:
        print("wrong!! You Asian ")
        quit(".")
    m = m + 1





