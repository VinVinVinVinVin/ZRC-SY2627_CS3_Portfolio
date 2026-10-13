class CD:
    def __init__(self, name):
        self.name = name  
    def cdstuff(self):
        return f"{self.name} is in the CD list."

    def bettercd(self):
        return f"{self.name} has improved CD access."


class SSD(CD):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department 
    def show_info(self):
        return f"{self.name} works in the {self.department} section."

    def task(self):
        return f"{self.name} is assigned SSD work."


class CID(CD):
    def __init__(self, name, role, age, campus):
        super().__init__(name)
        self.role = role
        self.age = age
        self.campus = campus

    def info(self):
        return f"{self.name} is a CID member with role {self.role}."

    def assign_task(self):
        return f"{self.name} is assigned to {self.campus} campus."


class Advisers(CID):
    def __init__(self, name, role, age, campus):
        super().__init__(name, role, age, campus)

    def advise(self):
        return f"{self.name} gives advice."


class Staff(CID):
    def __init__(self, name, role, age, campus):
        super().__init__(name, role, age, campus)

    def support(self):
        return f"{self.name} is a staff member."


class Students(CID):
    def __init__(self, name, role, age, campus):
        super().__init__(name, role, age, campus)

    def study(self):
        return f"{self.name} is studying."


class Parents(Students):
    def __init__(self, name, role, age, campus):
        super().__init__(name, role, age, campus)

    def support(self):
        return f"{self.name} is a family member."


cd = CD("John")
ssd = SSD("Sam", "Technology")
cid = CID("Mary", "Support", 22, "Main")
adviser = Advisers("Mr. Lee", "Advisor", 35, "North")
staff = Staff("Mr. Smith", "Instructor", 45, "South")
student = Students("Aisha", "Student", 18, "North")
parent = Parents("Mrs. Cohena", "Parent", 40, "North")

print(cd.cdstuff())
print(cd.bettercd())
print(ssd.show_info())
print(ssd.task())
print(cid.info())
print(cid.assign_task())
print(adviser.advise())
print(staff.support())
print(student.study())
print(parent.support())
