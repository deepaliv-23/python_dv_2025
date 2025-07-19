class form:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def admission(self):
        print(f"My name is {self.name} and my id is {self.id}")

class form1:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def admission(self):
        print(f"My name is {self.name}  and my id is {self.id}")    

class form2:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def admission(self):
        print(f"My name is {self.name} and my id is {self.id}")  

Student1=form("Deepali",1)
print(Student1.admission())

Student2=form1("Aditi",2)
print(Student2.admission())  

Student3=form("Hiral",3)
print(Student3.admission())