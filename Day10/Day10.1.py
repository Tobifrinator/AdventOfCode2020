def main():
	data=open('data.txt','r')
	adapters=data.read().split()
	adapters = list(map(int, adapters))
	adapters=adapters+[0]+[max(adapters)+3]
	adapters.sort()
	print(adapters)
	joltage_diff_sum=[]
	for i in range(len(adapters)-1):
		joltage_diff_sum=joltage_diff_sum+[(adapters[i+1]-adapters[i])]
	print(joltage_diff_sum.count(1)*joltage_diff_sum.count(3))
	joltage_diff_sum.sort()
	print(joltage_diff_sum)

if __name__ == "__main__":
	main()