# -----------------DISPLAYING NO.DIVISIBLE BY 11 AND NOT BY 2 IN RANGE(100 TO 500)------------
num=[]
for inp in range(100,501):
    if inp%11==0 and inp%2!=0:
        num.append(inp)
print(num)