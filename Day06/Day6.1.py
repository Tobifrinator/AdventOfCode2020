import re
data=open('data.txt','r')
groups=data.read().split("\n\n")

sum=0
for group in groups:
    #print("\n\n")
    persons=group.split()
    #print(persons)
    answered=persons[0]
    for person in persons:
        for question in person:
            if question not in answered:
                print(question,"from",person,"not in answered:",answered,"->",answered+question)
                answered=answered+question
    sum=sum+len(answered)
    print("group answered",len(answered), "different questions, sum is now",sum,"\n")

print("the total sum and answer is" ,sum)