import numpy as np
data_type=[("name","S15"),("class",int),("height",float)]
student_detail=[("tyron jamal ",6,48.5),("monkey",7,152.5),("bannannna",10,62.5)]
students=np.array(student_detail,dtype=data_type)
print("print original array")
print(students)
print("sort by height")
print(np.sort(print(students,order="height")))