even=[]
odd=[]
count=0
a=0
x=input("Enter Number:")
y=[]
z=x.split(",")
for i in z:
    y.append(int(i))
while len(y)>a:
    if y[a]%2==1:
        even.append(y[a])
    else:
        odd.append(y[a])    
    a=a+1
print("Even Number",even)
print("Odd numbers",odd)    
