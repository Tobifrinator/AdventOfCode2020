data=open('data.txt','r')
lines=data.read().split('\n')
row=[]

for i,line in enumerate(lines):
    row=row+[line]

i_increment=[1,1,1,1,2]
j_increment=[1,3,5,7,1]
trees=[0,0,0,0,0]

for rounds in range(0,5):
    i=j=0
    while(i<len(row)):
        if(row[i][j]=='#'):
            trees[rounds]=trees[rounds]+1
        j=(j+j_increment[rounds])%len(row[i])
        i=i+i_increment[rounds]
    print("Round",str(rounds+1)+":",str(trees[rounds]))

product=1
for trees_per_round in trees:
    product=product*trees_per_round
print("product of all:",str(product))