string=input("please entern your word:")
char=input("please enter your charicter:")
i=0
count=0
while(i<len(string)):
    if(string[i]==char):
        count=count+1
    i=i+1
print(count)