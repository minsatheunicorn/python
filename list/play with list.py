l=[54,235,23,5234,5]
print("orignal list",l)
count=0
for i in l:
 count+=i
abv=count/len(l)
print("sum=",count)
print("average=",abv)
l.sort()
print("spotted list",l)
print("first element",l[0])
print("second element",l[1])