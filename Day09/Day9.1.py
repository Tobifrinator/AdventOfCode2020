def valid_sum(sum, summands):
    for i,summand in enumerate(summands):
        for j in range(i+1, len(summands)):
            if(summand+summands[j]==sum):
                return True
    return False

def main():
    data=open('data.txt','r')
    numbers=data.read().split()
    numbers = list(map(int, numbers))
    summands, sums=numbers[:25], numbers[25:]
    print(summands)
    #print(sums)
    for sum in sums:
        if not valid_sum(sum,summands):
            print("The first invalid number is "+str(sum))
        summands=summands[1:]+[sum]

if __name__ == "__main__":
    main()