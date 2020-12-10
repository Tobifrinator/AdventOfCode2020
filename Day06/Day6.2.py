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
        for question in answered:
            if question not in person:
                print(question,"from",answered,"not in person:",person,"->",answered.replace(question,''))
                answered=answered.replace(question,'')
    sum=sum+len(answered)
    print("everyone in the group answered",len(answered), "same questions, sum is now",sum,"\n")
print("the total sum and answer is" ,sum)