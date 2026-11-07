class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount

    def display_patient_type(self):
        print("Patient Type: Regular Patient")


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80

    def display_patient_type(self):
        print("Patient Type: Senior Citizen")


class PhilhealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")


if __name__ == "__main__":
    print("Hospital Billing System")

    patients = [
        Patient("Juan Dela Cruz", 15000.0),
        SeniorPatient("Maria Santos", 15000.0),
        PhilhealthPatient("Pedro Reyes", 15000.0)
    ]

    for p in patients:
        print(f"Patient Name: {p.get_name()}")
        p.display_patient_type()
        print(f"Original Bill: P{p.get_bill_amount():,.2f}")
        print(f"Final Bill: P{p.calculate_bill():,.2f}")
