class employee:

    no_employee=0
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.email=fname + '.' + lname + '@gmail.com'

        employee.no_employee += 1

    def details(e):
        fullname=e.fname + " " + e.lname
        # fullname='{} {}'.format(e.fname,e.lname)
        print('Full name of the employee;',fullname)
        print('email of employee:',e.email)
        print('salary of the employee:', e.salary)
     
emp1=employee('pranav','maheta',50000)
emp2=employee('janvi','dave',90000)
emp3=employee('sakshi','maheta',70000)
# employee.details(emp1)
# print(employee.details(emp1))
# print(emp1.__dict__)
emp1.details()
emp2.details()
emp3.details()
# print(emp1.details())
print('total employee=',employee.no_employee)