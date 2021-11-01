import random as rd
import time
print ("welcome")
print ("rock,paper,sissor?")
print("please enter r,p,s")
n=(input())
cc=['r','p','s']
co=rd.choice(cc)
if n!='r' and n!='s' and n!='p':
    print("invalid input") 
else:
    time.sleep(1)
    print("computer choise is",co)
def op():
    if (co=='p' and n=='r') :
        print("you lost against paper!")
    elif(co=='r' and n=='s'):
        print("you lost against rock!")
    elif co=='s' and n=='p':
        print("you lost against sissor!")
    elif co=='s' and n=='r':
        print("you won against sissor!")
    elif co=='p' and n=='s':
        print("you won against paper!")
    elif co=='r' and n=='p':
        print("you won against rock!")   
    elif (co=='p'and n=='p') or (co=='r'and n=='r') or(co=='s' and n=='s'):
        print("tie!") 
if n=='r':
    op()
elif n=='p':
    op()
elif n=='s':
    op()