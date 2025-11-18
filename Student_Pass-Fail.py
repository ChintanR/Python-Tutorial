a = int(input("Enter marks of Subject1 : "))
b = int(input("Enter marks of Subject2 : "))
c = int(input("Enter marks of Subject3 : "))
d = int(input("Enter Total marks : "))

if(a>33 and b>33 and c>33) and (d>120):
    print("Congratulations, Student is Passed")
else:
    print("Sorry, Student is Failed")