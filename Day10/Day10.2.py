"""
possibilities calculates the number of possible steps from adapters[i] by adding the possible steps of adapters[i+1], adapters[i+2] and adapters[i+3]
recursion achor is the case when adapter[i] is the last adapter
"""
def possibilities(adapters):
	if(len(adapters)==1):
		return 1
	possible=possibilities(adapters[1:])
	if(len(adapters)>2):
		if(adapters[2]-adapters[0]<=3):
			possible=possible+possibilities(adapters[2:])
	if(len(adapters)>3):
		if(adapters[3]-adapters[0]<=3):
			possible=possible+possibilities(adapters[3:])
	return(possible)

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
	joltage_diffs=[]
	for i in range(len(adapters)-1):
		joltage_diffs=joltage_diffs+[(adapters[i+1]-adapters[i])]
	"""
	for speedup, we can split the array whenever a joltage_diff of 3 appears, since this path has to be taken. We can then calculate the number of possibilities in our fragments and multiply those with each other.
	Example 1-2-3-6-7-8
	since we have to get from 3 to 6, we can calculate the #possibilities from 1 to 3 and 6 to 8, Then, the #total_possibilities is #(1 to 3)*#(6 to 8)=4
	1-2-3-6-7-8
	1-3-6-7-8
	1-2-3-6-8
	1-3-6-8
	"""
	fragments=[]
	previous3=0
	for i,joltage_diff in enumerate(joltage_diffs):
		if(joltage_diff==3):
			fragments=fragments+[adapters[previous3:i+1]]
			previous3=i+1
	total=1
	for fragment in fragments:
		total=total*possibilities(fragment)
	print(total)

if __name__ == "__main__":
	main()