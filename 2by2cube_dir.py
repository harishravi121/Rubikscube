cube2=[[0 for j in range(8)] for i in range(6)]
cube=[[0 for j in range(8)] for i in range(6)]
def cubecopy():
    for i in range(6):
        for j in range(8):
            cube[i][j]=cube2[i][j];

def cubecopy2():
    for i in range(6):
        for j in range(8):
            cube2[i][j]=cube[i][j];


def changecorner(j,i) :
    cube2[i[0][0]][i[0][1]]=cube[j[0][0]][j[0][1]];
    cube2[i[1][0]][i[1][1]]=cube[j[1][0]][j[1][1]];
    cube2[i[2][0]][i[2][1]]=cube[j[2][0]][j[2][1]];


def rotateclockwise(a,b,c,d) :
    changecorner(d,a);
    changecorner(a,b);
    changecorner(b,c);
    changecorner(c,d);
    

def rotatecounterclockwise(a,b,c,d) :
    changecorner(d,a);
    changecorner(a,b);
    changecorner(b,c);
    changecorner(c,d);


for i in range(6):
    print(cube[i])
print()

for i in range(2):
    for j in range(2):
        cube[i][j+2]=1
        cube[i+2][j]=2
        cube[i+2][j+2]=3
        cube[i+2][j+4]=4
        cube[i+2][j+6]=5
        cube[i+4][j+2]=6

cubecopy2();

for i in range(100000):
    for i in range(6):
        print(cube2[i])

