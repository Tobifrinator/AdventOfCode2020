data=open('data.txt','r')
numbers=data.read().split('\n')
print(numbers)
for i in numbers:
    for j in numbers:
        for k in numbers:
            if (int(i)+int(j)+int(k))==2020:
                print(i,'*',j,'*',k,'=',int(i)*int(j)*int(k))