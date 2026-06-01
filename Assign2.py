class Employee:
    def __init__(self,empid=None,name=None,salary=None):
        self.empid=empid
        self.name=name
        self.salary=salary

    def SetEmpid(self,empid):
        self.empid=empid
    def SetNAme(self,name):
        self.name=name
    def SetSalary(self,salary):
        self.salary= salary
    def getEmpid(self):
        return self.empid
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
    
e1=Employee()
e2=Employee(1,"Rahul",40000)
e1.SetEmpid(2)
e1.SetNAme("Ramesh")
e1.SetSalary(50000)
print(e1.getEmpid(),e1.getName(),e1.getSalary())
print(e2.getEmpid(),e2.getName(),e2.getSalary())