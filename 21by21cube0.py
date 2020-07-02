import random
cube2=[[0 for j in range(63)] for i in range(84)]
cube=[[0 for j in range(63)] for i in range(84)]
for i in range(0,84):
        print(cube[i])
for i in range(21):
    for j in range(21):
        cube[i][j+21]=1
        cube[i+21][j]=2
        cube[i+21][j+21]=3
        cube[i+21][j+42]=4
        cube[i+42][j+21]=5
        cube[i+63][j+21]=6
for i in range(0,84):
        print(cube[i])
#for i in range(0,9):
 #   print(cube[i])

#RURiURUURi, FURUiRiFi, RiFRiBBRFiRiBBRRUi,FFUiLRiF    

# or 8+12 * 12 = 240 lines of code only front and front anticlockwise written others need to be rewritten as an assignment before playing

print('12 moves F f B b U u D d R r L l')
def changeedge(j,i) :
    cube2[i[0][0]][i[0][1]]=cube[j[0][0]][j[0][1]];
    cube2[i[1][0]][i[1][1]]=cube[j[1][0]][j[1][1]];

def changecorner(j,i) :
    cube2[i[0][0]][i[0][1]]=cube[j[0][0]][j[0][1]];
    cube2[i[1][0]][i[1][1]]=cube[j[1][0]][j[1][1]];
    cube2[i[2][0]][i[2][1]]=cube[j[2][0]][j[2][1]];

    
def rotateclockwise(a,b,c,d,e,f,g,h) :
    changecorner(g,a);
    changeedge(h,b);
    changecorner(a,c);
    changeedge(b,d);
    changecorner(c,e);
    changeedge(d,f);
    changecorner(e,g);
    changeedge(f,h);

def rotatecounterclockwise(a,b,c,d,e,f,g,h) :
    changecorner(a,g);
    changeedge(b,h);
    changecorner(c,a);
    changeedge(d,b);
    changecorner(e,c);
    changeedge(f,d);
    changecorner(g,e);
    changeedge(h,f);

def cubecopy(n,m):
    for i in range(n):
        for j in range(m):
            cube[i][j]=cube2[i][j];
    
def moves2(x):
    
    if x=='F':  # Front
        rotateclockwise([[3,3],[3,2],[2,3]],[[3,4],[2,4]],[[3,5],[2,5],[3,6]],[[4,5],[4,6]],[[5,5],[6,5],[5,6]],[[5,4],[6,4]],[[5,3],[6,3],[5,2]],[[4,3],[4,2]]);
        

    if x=='f':  # Front'
        rotatecounterclockwise([[3,3],[3,2],[2,3]],[[3,4],[2,4]],[[3,5],[2,5],[3,6]],[[4,5],[4,6]],[[5,5],[6,5],[5,6]],[[5,4],[6,4]],[[5,3],[6,3],[5,2]],[[4,3],[4,2]]);



    if x=='B':  # Back
        rotateclockwise([[11,5],[3,8],[0,5]],[[11,4],[0,4]],[[11,3],[0,3],[3,0]],[[10,3],[4,0]],[[9,3],[5,0],[8,3]],[[9,4],[8,4]],[[9,5],[8,5],[5,8]],[[10,5],[4,8]]);


    if x=='b': #Back'
        rotatecounterclockwise([[11,5],[3,8],[0,5]],[[11,4],[0,4]],[[11,3],[0,3],[3,0]],[[10,3],[4,0]],[[9,3],[5,0],[8,3]],[[9,4],[8,4]],[[9,5],[8,5],[5,8]],[[10,5],[4,8]]);

    if x=='U':  # Up
        rotateclockwise([[0,3],[3,0],[11,3]],[[0,4],[11,4]],[[0,5],[11,5],[3,8]],[[1,5],[3,7]],[[2,5],[3,6],[3,5]],[[2,4],[3,4]],[[2,3],[3,3],[3,2]],[[1,3],[3,1]]);


    if x=='u': #Up'
        rotatecounterclockwise([[0,3],[3,0],[11,3]],[[0,4],[11,4]],[[0,5],[11,5],[3,8]],[[1,5],[3,7]],[[2,5],[3,6],[3,5]],[[2,4],[3,4]],[[2,3],[3,3],[3,2]],[[1,3],[3,1]]);

    if x=='D':  # Down
        rotateclockwise([[6,3],[5,2],[5,3]],[[6,4],[5,4]],[[6,5],[5,5],[5,6]],[[7,5],[5,7]],[[8,5],[5,8],[9,5]],[[8,4],[9,4]],[[8,3],[9,3],[5,0]],[[7,3],[5,1]]);


    if x=='d': #Down'    
        rotatecounterclockwise([[6,3],[5,2],[5,3]],[[6,4],[5,4]],[[6,5],[5,5],[5,6]],[[7,5],[5,7]],[[8,5],[5,8],[9,5]],[[8,4],[9,4]],[[8,3],[9,3],[5,0]],[[7,3],[5,1]]);

    if x=='R':  # Right
        rotateclockwise([[3,6],[3,5],[2,5]],[[3,7],[1,5]],[[3,8],[0,5],[11,5]],[[4,8],[5,7]],[[5,8],[9,5],[8,5]],[[5,7],[7,5]],[[5,6],[6,5],[5,5]],[[4,6],[4,5]]);


    if x=='r': #Right'
        rotatecounterclockwise([[3,6],[3,5],[2,5]],[[3,7],[1,5]],[[3,8],[0,5],[11,5]],[[4,8],[5,7]],[[5,8],[9,5],[8,5]],[[5,7],[7,5]],[[5,6],[6,5],[5,5]],[[4,6],[4,5]]);

    if x=='L':  # Left
        rotateclockwise([[3,0],[11,3],[0,3]],[[3,1],[1,3]],[[3,2],[2,3],[3,4]],[[4,2],[4,3]],[[5,2],[5,3],[6,3]],[[5,1],[7,3]],[[5,0],[8,5],[9,5]],[[4,0],[10,3]]);


    if x=='l': #Left'         
        rotatecounterclockwise([[3,0],[11,3],[0,3]],[[3,1],[1,3]],[[3,2],[2,3],[3,4]],[[4,2],[4,3]],[[5,2],[5,3],[6,3]],[[5,1],[7,3]],[[5,0],[8,5],[9,5]],[[4,0],[10,3]]);

    cubecopy(12,9)
    for i in range(0,12):
        print(cube[i])
        


op='F';

def map2(y):
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

    print(op)

