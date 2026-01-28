student_data={
    "id1":"marion","id2":"malita","id3":"marion","id4":"mariam"
}
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)