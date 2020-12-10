data=open('data.txt','r')
lines=data.read().split('\n')
correct=0
for line in lines:
    count=0
    blocks=line.split(' ')
    character=blocks[1][:-1]
    min=int(blocks[0].split('-')[0])
    max=int(blocks[0].split('-')[1])
    pw=blocks[2]
    for i in pw:
        if i==character:
            count=count+1
    if(count>=min and count<=max):
        correct=correct+1
    print("Min:",min,"max:",max,"character", character,"pw:", pw, count)
    print(correct)
print(correct)