import time
import random
n=3
a=['R','L','F','B','U','D']
f5=['','1']
b=['','i']
f3=['','']
f=[]
if(n==3):
    f=f3
else:
    f=f5
c=''
for i in range(10):
    c=''
    for j in range(10):
        c=c+random.choice(a)+random.choice(f)+random.choice(b)
    print(c)
    d=input()
    print('Start')
    start=time.time()
    e=input()
    stop=time.time()
    cubetime=stop-start

    
    print('Time = ',round(cubetime,2),'Score 1= ',round(n**n*100/cubetime,2),'Score 2= ',round(n**n/cubetime**2,2))


'''



What is the right game theory scoring sytem based on order of cube others etc. We should just self motivate for least time.

Happy to sell or gift code on github or email

Dr. Harish Ravi

Remains to see if I get self motivated to reach lowest time by sharing ocassionally and maintaining a log in a file next.


'''
