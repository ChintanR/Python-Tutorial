class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode
        
c = Programmer("Chintan", 1200000, 411019)
print(c.name, c.company, c.salary, c.pincode)
m = Programmer("Mithilesh", 1500000, 411023)
print(m.name, m.company, m.salary, m.pincode)