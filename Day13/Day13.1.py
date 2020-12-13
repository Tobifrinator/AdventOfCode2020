def main():
	"""
	parse input data:
	first line is arrival time, second line has the busIDs and x's, convert the busIDs to integers and make a list
	set starting values for the minimal wait time and the busID
	we want to use a waittime that will be overwritten, therefore we can use any busID, since:
	waittime < the smallest busID <= any busID
	"""
	data=open('data.txt','r')
	lines=data.read().split()
	arrival_time=int(lines[0])
	busses=lines[1].split(',')
	for i in range(len(busses)):
		if(busses[i]!='x'):
			busses[i]=int(busses[i])
			min_waittime=busses[i]
			bus_id=busses[i]

	"""
	we can calculate the waitingtime for a given bus using (bus-arrival_time)%bus, arrival_time%bus is how many minutes have passed since the last bus came, therefore(bus-arrival_time)%bus is the remaining waitingtime for this bus
	if its smaller than the current min_waitingtime its the new min_waitingtime
	"""
	for bus in busses:
		if(bus!='x'):
			waittime=(bus-arrival_time)%bus
			if(waittime<min_waittime):
				min_waittime=waittime
				bus_id=bus
	print("ID:",bus_id, "\nwaittime:", min_waittime, "\nID * waittime =",min_waittime*bus_id)


if __name__ == "__main__":
	main()