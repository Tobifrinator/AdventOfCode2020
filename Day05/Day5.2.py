import re

data=open('data.txt','r')
seats=data.read().split()
occupied=[0]*(127*8+7)
for seat in seats:
    row=0
    column=0
    for i in range(0,7):
        if seat[i]=='B':
            row=row+2**(6-i)
    for i in range(0,3):
        if seat[7+i]=='R':
            column=column+2**(2-i)
    seat_id=8*row+column
    occupied[seat_id]=1
    #print(seat,row, column, seat_id)

for i in range(1,len(occupied)-1):
    if(occupied[i]==0 and occupied[i-1]==1 and occupied[i+1]==1):
        print(i)

