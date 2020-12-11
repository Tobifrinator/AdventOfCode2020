from copy import copy, deepcopy
def change_seating(seating):
	changed=False
	changing=[]
	for i in range(len(seating)):
		row=[0]*len(seating[0])
		changing=changing+[row]
	for row in range(1,len(seating)):
		for column in range(1,len(seating[row])):
			if seating[row][column]=='L':
				if occupied_neighbors(seating,row,column)==0:
					changing[row][column]=1
					changed=True
			if seating[row][column]=='#':
				if occupied_neighbors(seating,row,column)>=4:
					changing[row][column]=1
					changed=True
	for row in range(1,len(seating)):
		for column in range(1,len(seating[row])):
			if seating[row][column]=='L':
				if changing[row][column]==1:
					seating[row]=seating[row][:column]+'#'+seating[row][column+1:]
			else:
				if seating[row][column]=='#':
					if changing[row][column]==1:
						seating[row]=seating[row][:column]+'L'+seating[row][column+1:]
	return changed


def occupied_neighbors(seating, seatrow, seatcolumn):
	occupied=0
	for i in range(9):
		if(i==4):
			continue
		if(seating[i//3+seatrow-1][i%3+seatcolumn-1]=='#'):
			occupied=occupied+1
	if(1==0):
		print("\n"+seating[seatrow-1][seatcolumn-1:seatcolumn+2])
		print(seating[seatrow][seatcolumn-1:seatcolumn+2])
		print(seating[seatrow+1][seatcolumn-1:seatcolumn+2])
		print("->",occupied)
	return occupied

def main():
	data=open('data.txt','r')
	#print(data.read())
	seating=data.read().split()
	seating.insert(0,len(seating[0])*'.')
	seating.append(len(seating[0])*'.')
	for i,row in enumerate(seating):
		seating[i]='.'+seating[i]+'.'
	changed=True
	while(changed):
		changed=change_seating(seating)
		for i in range(len(seating)):
			pass
	count=0
	for row in seating:
		count=count+row.count('#')
	print(count)
if __name__ == "__main__":
	main()