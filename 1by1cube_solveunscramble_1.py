cube2=[[0 for j in range(3)] for i in range(4)]
cube=[[0 for j in range(3)] for i in range(4)]
cubei=[[0 for j in range(3)] for i in range(4)]
solved=1
import random

def cubecopy():
    for i in range(4):
        for j in range(3):
            cube[i][j]=cube2[i][j];

def cubecopy2():
    for i in range(4):
        for j in range(3):
            cube2[i][j]=cube[i][j];

def cubecopyi():
    for i in range(4):
        for j in range(3):
            cubei[i][j]=cube[i][j];

def cubecheck():
    global solved
    solved=1
    for i in range(4):
        for j in range(3):
            if(cubei[i][j]!=cube[i][j]):
                solved=0

def changeface(j,i) :
    cube2[i[0]][i[1]]=cube[j[0]][j[1]];



def rotateclockwise(a,b,c,d) :
    changeface(d,a);
    changeface(a,b);
    changeface(b,c);
    changeface(c,d);
    

def rotatecounterclockwise(a,b,c,d) :
    changeface(a,d);
    changeface(b,a);
    changeface(c,b);
    changeface(d,c);




cube[0][1]=1
cube[1][0]=2
cube[1][1]=3
cube[1][2]=4
cube[2][1]=5
cube[3][1]=6

def printcube():
    print()
    for i in range(4):
        print(cube[i])
    print()

cubecopy2()
cubecopyi()

def cubecopy(n,m):
    for i in range(n):
        for j in range(m):
            cube[i][j]=cube2[i][j];
    
def moves2(x):
    
    if x=='F':  # Front
        rotateclockwise([1,0],[0,1],[1,2],[2,1]);
    if x=='f':  # Front'
        rotatecounterclockwise([1,0],[0,1],[1,2],[2,1]);



    if x=='B':  # Back
        rotateclockwise([1,2],[0,1],[1,0],[2,1]);


    if x=='b': #Back'
        rotatecounterclockwise([1,2],[0,1],[1,0],[2,1]);

    if x=='U':  # Up
        rotateclockwise([1,1],[1,0],[3,1],[1,2]);


    if x=='u': #Up'
        rotatecounterclockwise([1,1],[1,0],[3,1],[1,2]);

    if x=='D':  # Down
        rotateclockwise([1,1],[1,2],[3,1],[1,0]);

    if x=='d': #Down'    
        rotatecounterclockwise([1,1],[1,2],[3,1],[1,0]);

    if x=='R':  # Right
        rotateclockwise([1,1],[0,1],[3,1],[2,1]);

    if x=='r': #Right'
        rotatecounterclockwise([1,1],[0,1],[3,1],[2,1]);
    if x=='L':  # Left
        rotateclockwise([1,1],[2,1],[3,1],[0,1]);

    if x=='l': #Left'         
        rotatecounterclockwise([1,1],[2,1],[3,1],[0,1]);
    cubecopy(4,3)

        


op='F';

def map2(y):
    global op
    if y==0:
        op='F';
    if y==1:
        op='f';
    if y==2:
        op='B';
    if y==3:
        op='b';        
    if y==4:
        op='U';
    if y==5:
        op='u';
    if y==6:
        op='D';
    if y==7:
        op='d';
    if y==8:
        op='R';
    if y==9:
        op='r';
    if y==10:
        op='L';
    if y==11:
        op='l';



def undo(x):
    if(x%2==0):
        return x+1
    else:
        return x-1


printcube()

moveno=1000

m=[0 for j in range(moveno)]
um=[0 for j in range(moveno)]
for i in range(len(m)):
        
    m[i]=random.randint(0,11)
    map2(m[i])
    moves2(op)
print(m)
printcube()

for i in range(len(m)):
        
    um[i]=undo(m[len(m)-i-1])
    map2(um[i])
    moves2(op)
print(um)    
printcube()

