import os
def main():
    cwd = os.getcwd()
    for day in range(1,25):
        path=cwd+"/Day"+("0"+str(day) if day<10 else str(day))
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)
            d1 = open(path+"/Day"+str(day)+".1.py", "a")
            d1.write("def main():\n\tdata=open('data.txt','r')\n\tprint(data.read())\n\n\nif __name__ == \"__main__\":\n\tmain()")
            d2 = open(path+"/Day"+str(day)+".2.py", "a")
            d2.write("def main():\n\tdata=open('data.txt','r')\n\tprint(data.read())\n\n\nif __name__ == \"__main__\":\n\tmain()")
            data=open(path+"/data.txt", "x")
            example=open(path+"/example.txt", "x")
            d1.close()
            d2.close()
            data.close()

if __name__ == "__main__":
    main()