from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
        
    def Book(self, fro, to):
        print(f"Ticket is booked in Train No.: {self.trainNo} from {fro} to {to}.")
        
    def getStatus(self):
        print(f"Train No.: {self.trainNo} is running on time.")
        
    def Fare(self, fro, to):
        print(f"Ticket fare in Train No.: {self.trainNo} from {fro} to {to} is {randint(222,555)}")
        
t = Train(1276)
t.Book("Pune", "Mumbai")
t.getStatus()
t.Fare("Pune", "Mumbai")