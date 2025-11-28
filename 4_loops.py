a = int(input("Enter a number: "))

for i in range(2, a):
    if(a%i==0):
        print("Given number is not prime number")
        break
    
else:
    print("Given number is prime number")
        