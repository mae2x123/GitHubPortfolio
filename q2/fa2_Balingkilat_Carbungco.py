class Patient:
    def __init__(self,name:str, bill_amount:float):
        self._name=name
        self._bill_amount=bill_amount
    def get_name(self):
        return self._name
    def set_name(self,name=str):
        self._name=name
    def get_bill_amount(self):
        return self._bill_amount
    def set_bill_amount(self,bill_amount=float):
        self._bill_amount=float(bill_amount)
    def calculate_bill(self):
        return self._bill_amount


class Senior_Patient(Patient):
    def calculate_bill(self):
        return self._bill_amount*0.80

class PhilHealth_Patient(Patient):
    def calculate_bill(self):
        return self._bill_amount*0.85

if __name__ == "__main__":
    regular_patient = Patient("Juan Dela Cruz", 15000)
    senior_patient = Senior_Patient("Maria Santos", 15000)
    philhealth_patient = PhilHealth_Patient("Pedro Reyes", 15000)

    print("Hospital Billing System")
    print("-----------------------")

    patients=[regular_patient,senior_patient,philhealth_patient]

    for p in patients:
        print(f"Patient Name: {p.get_name()}")
        print(f"Original Bill: {p.get_bill_amount():,.2f}")
        print(f"Final Bill: {p.calculate_bill():,.2f}")
        print()

        
        

 
    
        
