data=open('data.txt','r')
commands=data.read().split("\n")
executed=[0]*len(commands)
i=0
acc=0
#run the program, stop when the command was already executed
while executed[i]==0:
    executed[i]=1
    command, argument=commands[i].split()
    print(str(i)+":", command, argument)
    if(command=="jmp"):
        i=i+int(argument)
    else:
        if command=="acc":
            acc=acc+int(argument)
        i=i+1

print("\nThe sum is",acc)