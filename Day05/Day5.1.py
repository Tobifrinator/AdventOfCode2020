import re

data=open('data.txt','r')
seats=data.read().split()
#print(seats)
highest_seat_id=0
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
    if seat_id>highest_seat_id:
        highest_seat_id=seat_id
    #print(seat,row, column, seat_id)

print(highest_seat_id)
