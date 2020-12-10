
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
	adapters=adapters+[0]+[max(adapters)+3]
	adapters.sort()
	joltage_diffs=[]
	for i in range(len(adapters)-1):
		joltage_diffs=joltage_diffs+[(adapters[i+1]-adapters[i])]

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