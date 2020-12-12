def main():
	data=open('data.txt','r')
	movements=data.read().split()
	#North South East and West are now polar coordiantes
	cardinal={
		"N":1j,
		"S":-1j,
		"E":1,
		"W":-1
	}
	# R-Rotation changes East to South -> -1j,L-Rotation changes East to North -> +1j
	rotation={
		"R":-1j,
		"L":1j
	}
	facing=1
	manhattan_distance=0+0j
	for movement in movements:
		#move in the given direction
		if movement[0] in "NSEW":
			manhattan_distance=manhattan_distance+int(movement[1:])*cardinal[movement[0]]
		#turn n*90 degrees, -> rotation ** n
		if movement[0] in "LR":
			facing=facing*(rotation[movement[0]]**(int(movement[1:])/90))
		#move forward in the facing direction
		if movement[0] in "F":
			manhattan_distance=manhattan_distance+facing*int(movement[1:])
	NS=manhattan_distance.imag
	EW=manhattan_distance.real
	#manhattan_distance=|NS|+|EW|
	print("The ship moved",NS,"towards north and ",EW," towards east. The manhattan distance is", abs(NS)+abs(EW))

if __name__ == "__main__":
	main()