list=[]
x=int(input("Enter Number"))
for i in range (1,x+1):
    a=x%i
    if a==0:
        list.append(i)
        print(list)
print(list)
if len(list)==2:
    print("prime")
else:
    print("not a prime")        