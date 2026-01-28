x={"1":67,"2":67,"3":67,"4":76,"5":76}
print("the oringinal dictionary",x)
k=67
result=0
for key in x:
    if x[key]==k:
        result=result+1
print("frequency of 67 is ",result)