def apply_mask(destination,mask):
	# every bit where mask=1 has to become 1 -> OR, replace x by 0 so that it doesnt interfere
	destination=destination | int(mask.replace('X','0'), base=2)
	for j,char in enumerate(mask):
		if char=='X':
			# for every x, return the results if the bit was flipped and if it wasnt <-> if destination bit is 1 and if it is 0
			return apply_mask(destination^(1<<(len(mask)-1-j)), mask[:j]+'0'+mask[j+1:]) + apply_mask(destination, mask[:j]+'0'+mask[j+1:])
	return [destination]


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
			#apply the mask to the destination of this line
			for masked_destination in apply_mask(int(destination[4:-1]),mask):
				mem[masked_destination]=int(sources[i])

	print(mem)
	print("The sum of all values left in memory is",sum(mem.values()))

if __name__ == "__main__":
	main()