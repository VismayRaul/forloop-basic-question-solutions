# --------------------------------------PRIME NUMBER------------------------------------------
number_input= int(input("Enter no. to check its prime or not : "))
if number_input>1:
    for i in range(2,number_input):
        if number_input%i ==0:
            z="its a not a prime number"
            break
        else:
            z='it is a prime number'             
if number_input==2:
    z='it is a prime number'
print(z)