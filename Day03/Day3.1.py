data=open('data.txt','r')
lines=data.read().split('\n')
row=[]
for i,line in enumerate(lines):
    row=row+[line]
i=j=0
trees=0
while(i<len(row)):
    if(row[i][j]=='#'):
        trees=trees+1
    j=(j+3)%len(row[i])
    i=i+1
print('#trees:',trees)