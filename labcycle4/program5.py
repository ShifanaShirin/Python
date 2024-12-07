n=int(input("Enter the number of elements:"))
lst=[]
for i in range(n):
	a=int(input("Enter the element:"))
	lst.append(a)
power=map(lambda x:2**x,lst)
print("Powers of 2:")
powers=list(power)
print(powers)
