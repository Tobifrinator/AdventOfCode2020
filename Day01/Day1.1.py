data=open('data.txt','r')
numbers=data.read().split('\n')
print(numbers)
for i in numbers:
    for j in numbers:
        if (int(i)+int(j))==2020:
            print(i,'*',j,'=',int(i)*int(j))