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

    for sum in sums:
        if not valid_sum(sum,summands):
            print("The first invalid number is "+str(sum))
            invalid_number=sum
            break
        summands=summands[1:]+[sum]

    for i in range(len(numbers)):
        contigous_set=[numbers[i]]
        sum=numbers[i]
        j=i+1
        while(sum<invalid_number):
            sum=sum+numbers[j]
            contigous_set=contigous_set+[numbers[j]]
            if(sum==invalid_number):
                print("The sum of this set equals",str(invalid_number)+":", contigous_set,"\nThe set starts at",str(i),"and ends at",str(j)+".")
                contigous_set.sort()
                print("Sum of lowest and highset value in set:",contigous_set[0],"+",contigous_set[-1],"=",contigous_set[0]+contigous_set[-1])
            j=j+1

if __name__ == "__main__":
    main()