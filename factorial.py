# -------------------------------------FACTORIAL--------------------------------------------
factor = int(input("Enter no. whose facrotials you need : "))
factorial =1
for f in range(1,factor+1):
    factorial = factorial*f
print("factorial of ",factor,"is : ",factorial)