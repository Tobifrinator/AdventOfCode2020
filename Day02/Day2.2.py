data=open('data.txt','r')
lines=data.read().split('\n')
correct=0
for line in lines:
    xor_occurence=0
    blocks=line.split(' ')
    character=blocks[1][:-1]
    pos1=int(blocks[0].split('-')[0])
    pos2=int(blocks[0].split('-')[1])
    pw=blocks[2]
    if(pw[pos1-1]==character):
        xor_occurence=xor_occurence^1
    if(pw[pos2-1]==character):
        xor_occurence=xor_occurence^1
    print(line+":",bool(xor_occurence))
    correct=correct+xor_occurence
print('\n\nGesamt:',correct)
