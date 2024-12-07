n=int(input("Enter the number of elements:"))
l=[]
for i in range(n):
	a=int(input("Enter the element:"))
	l.append(a)
print("List :",l)
s=0
for i in l:
	s=s+i
print("Sum of elements of this list :",s)
