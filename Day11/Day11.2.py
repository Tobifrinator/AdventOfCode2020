def change_seating(seating):
	"""
	initialize a list for seats which need to be changed
	"""
	changed=False
	needs_changing=[]
	for i in range(len(seating)):
		row=[0]*len(seating[0])
		needs_changing=needs_changing+[row]

	"""
	mark seats that need to be changed according to the rules
	"""
	for row in range(0,len(seating)):
		for column in range(0,len(seating[row])):

			if seating[row][column]=='L':
				if occupied_neighbors(seating,row,column)==0:
					needs_changing[row][column]=1
					changed=True
			if seating[row][column]=='#':
				if occupied_neighbors(seating,row,column)>=5:
					needs_changing[row][column]=1
					changed=True
	"""
	execute the change
	"""
	for row in range(0,len(seating)):
		for column in range(0,len(seating[row])):

			if seating[row][column]=='L':
				if needs_changing[row][column]==1:
					seating[row]=seating[row][:column]+'#'+seating[row][column+1:]
			else:
				if seating[row][column]=='#':
					if needs_changing[row][column]==1:
						seating[row]=seating[row][:column]+'L'+seating[row][column+1:]

	return changed #returns true when a change has occured, this lets the while-loop continue



def occupied_neighbors(seating, seatrow, seatcolumn):
	occupied=0
	"""
	directions:
	0=[-1][-1], 1=[-1][0], 2=[-1][1], 3=[0][-1], 5=[0][1], 6=[1][-1], 7=[1][0], 8=[1][1]
	"""
	directions=[0,1,2,3,5,6,7,8]# 0=[-1],[-1]
	for i in directions:
		seat=seating[i//3-1+seatrow][i%3-1+seatcolumn]
		modifier=1
		#search for the next seat (#, L) or the edge (0)
		while(seat=='.'):
			seat=seating[(i//3-1)*modifier+seatrow][(i%3-1)*modifier+seatcolumn]
			modifier=modifier+1
		#if the seat is occupied, add one
		if(seat=='#'):
			occupied=occupied+1
	return occupied

def main():
	"""
	pad outer edges with 0 so that we can reuse occupied_neighbors()
	"""
	data=open('data.txt','r')
	seating=data.read().split()
	seating.insert(0,len(seating[0])*'0')
	seating.append(len(seating[0])*'0')
	for i,row in enumerate(seating):
		seating[i]='0'+seating[i]+'0'

	"""
	change the seating with our rules as long as change is happening
	"""
	changed=True
	while(changed):
		changed=change_seating(seating)

	"""
	count occupied seats
	"""
	count=0
	for row in seating:
		count=count+row.count('#')
	print(count,"seats are occupied.")


if __name__ == "__main__":
	main()

