# buhaton: we need to check if we need more patient types later (maybe PWD discount?)

class Patient:
    def __init__(self, name, bill_amount): 
        self.__name = name         
        self.bill = bill_amount   

    def get_name(self):
        return self.__name

    def get_bill_amount(self):
        return self.bill

    def calculate_bill(self):
        return self.bill


class SeniorPatient(Patient):
    def calculate_bill(self):
        discount = 0.20
        total = self.bill - (self.bill * discount)
        return total 
    
class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.bill * 0.85


print("Hospital Billing System Test\n")
print("-" * 30)

# creating sample object for our code
p1 = Patient("Juan Dela Cruz", 15000.0)
p2 = SeniorPatient("Maria Santos", 15000.0)
p3 = PhilHealthPatient("Pedro Reyes", 15000.0)

# for easier testing, we can put all patients in a list and loop thru them
all_patients = [p1, p2, p3]

for patiente in all_patients:
    print("Patient Name:", patiente.get_name())
    print("Original Bill: ₱" + str(patiente.get_bill_amount()))
    print("Final Bill: ₱{:,.2f}".format(patiente.calculate_bill()))
    print() # extra space