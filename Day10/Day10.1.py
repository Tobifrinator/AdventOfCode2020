def main():
	data=open('data.txt','r')
	adapters=data.read().split()
	adapters = list(map(int, adapters))
	#the outlet has joltage 0, the built in adapter has 3 more joltage than the hightest adapter
	#add them to the list of adapters
	adapters=adapters+[0]+[max(adapters)+3]
	#sort adapters by joltage
	#measure joltage difference between each pair of adapters
	adapters.sort()
	joltage_diff=[]
	for i in range(len(adapters)-1):
		joltage_diff=joltage_diff+[(adapters[i+1]-adapters[i])]
	print("Answer=occurence(1)*occurence(3) in joltage_diff:",joltage_diff.count(1),"*",joltage_diff.count(3),"=",joltage_diff.count(1)*joltage_diff.count(3))

if __name__ == "__main__":
	main()