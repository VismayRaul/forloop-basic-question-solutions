#-------------------------FINDING NUMBER OF EVEN ODD FROM THE SERIES--------------------
a=[6,5,9,5,20,3,5,2,2,1,3,21,8,7,57,63,55,69,8,9,5,7,6,2,6,3,4]
even=[]
odd=[]
for x in range(len(a)):
    if a[x]%2==0:
        e=a[x]
        even.append(e)
    else:
        o=a[x]
        odd.append(o)
print("even no. are : ",len(even))
print("odd no. are : ", len(odd))