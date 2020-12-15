def main():
	data=open('data.txt','r')
	numbers=data.read().split(',')
	memory={}
	current_number=0
	next_number=0

	wanted_number=30000000
	for i in range(0,wanted_number):

		#initialize the starting numbers, next_number after initializing will always be 0
		if(i<len(numbers)):
			memory[int(numbers[i])]=i
			continue
		current_number=next_number

		#if next_number is not in memory, its the first time this number has been said -> next number is 0
		if(next_number not in memory):
			next_number=0
		#else, the next number is age = current_round - last_round_it_was_said
		else:
			next_number=i-memory[current_number]

		#update the last round the number was said in
		memory[current_number]=i
	print(wanted_number,"->",current_number)

if __name__ == "__main__":
	main()