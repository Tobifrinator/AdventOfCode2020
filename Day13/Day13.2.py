from sympy.ntheory.modular import crt
def main():
	"""
	parse input data:
	second line has the busIDs and x's, convert the busIDs to integers and make a list,
	"""
	data=open('data.txt','r')
	lines=data.read().split()
	busses=lines[1].split(',')
	for i in range(len(busses)):
		if(busses[i]!='x'):
			busses[i]=int(busses[i])
	"""
	create system of linear congruencies:
	at timestamp t every bus has to come in i minutes, i being the position of the bus in the list
	therefore, at t the following equation has to be true:
	busID-i=t mod busID
	we can solve this system of equations using the chinese remainder theorem. The solution is our timestamp t
	"""
	busID=[]
	value_at_timestamp=[]
	for i, bus in enumerate(busses):
		if(bus!='x'):
			busID=busID+[bus]
			value_at_timestamp=value_at_timestamp+[(bus-i)%bus]
	print("The earliest timestamp at which all listed busIDs depart at offsets matching their position in the list is:\nt =", crt(busID,value_at_timestamp)[0])

if __name__ == "__main__":
	main()