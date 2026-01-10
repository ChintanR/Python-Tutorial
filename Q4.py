def factorial(n):
    i = 1
    sum = 0
    while(i<=n):
        sum += i
        i+=1
    return sum 
n = int(input("Enter a number: "))
print(f"Sum of natural numbers till {n} is {factorial(n)}")