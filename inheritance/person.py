class person:
   def __init__(self,name,idnumber):
     self.name=name
     self.idnumber=idnumber
   def display(self):
      print(self.name)
      print(self.idnumber)
class employed(person):
   def __init__(self,name,idnumber,salary,post):
    self.salary=salary
    self.post=post
    person.__init__(self,name,idnumber)
a=employed("komi",101,20000,"manager")
a.display()