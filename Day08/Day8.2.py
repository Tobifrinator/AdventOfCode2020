data=open('data.txt','r')
commands=data.read().split("\n")


#swaps jmp and nop in the string
def swap_jmp_nop(command):
    if command.split()[0]=="jmp":
        return "nop "+command.split()[1]
    if command.split()[0]=="nop":
        return "jmp "+command.split()[1]


for i,command in enumerate(commands):
    #swap every jump and nop and try if it runs to the end without an infinite loop
    #if it works, this is the correct swap, print the result of acc
    if command.split()[0]!="acc":
        commands[i]=swap_jmp_nop(command)
        executed=[0]*len(commands)
        j=0
        acc=0
        #run the commands until either at the end or command already executed once
        while j!=len(commands):
            if(executed[j]==1):
                acc=-1
                break
            executed[j]=1
            instruction, argument=commands[j].split()
            if(instruction=="jmp"):
                j=j+int(argument)
            else:
                if instruction=="acc":
                    acc=acc+int(argument)
                j=j+1
        #restore the original command
        commands[i]=command
        if(acc!=-1):
            print("The sum is",str(acc)+". To prevent an infinite loop, we had to change the command \""+command+"\" to \""+swap_jmp_nop(command)+"\" at line",str(i))
            break

