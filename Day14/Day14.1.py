def main():
	data=open('data.txt','r')
	lines=data.read().split('\n')
	destinations, sources=[], []
	#no mask applied yet; mem is a dictionary so that we can take 'mem[index]' as our key and not have a bloated array, since many fields in mem aren't used
	mask=''
	mem={}
	for line in lines:
		destinations=destinations+[line.split(' = ')[0]]
		sources=sources+[line.split(' = ')[1]]

	for i,destination in enumerate(destinations):
		#a new mask is applied from this point on
		if destination=='mask':
			mask=sources[i]
		if "mem" in destination:
			#apply the mask to the value of this line
			for j,char in enumerate(mask):
				if char=='X':
					pass
				if char=='1':
					# put 1 at corresponding bit
					sources[i]=str(int(sources[i]) | 1<<(len(mask)-1-j))
				if char=='0':
					# put 0 at corresponding bit
					sources[i]=str(int(sources[i]) & (0xFFFFFFFFF^1<<(len(mask)-1-j)))
			mem[destination]=int(sources[i])
	print("The sum of all values left in memory is",sum(mem.values()))

if __name__ == "__main__":
	main()