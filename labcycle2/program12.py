number1=input("Enter integers seperated by spaces which is to be inserted to first list:").split()
l1=[]
for i in number1:
	l1.append(int(i))
number2=input("Enter integers seperated by spaces which is to be inserted to second list:").split()
l2=[]
for i in number2:
        l2.append(int(i))
print(f"First List: {l1}\nSecond List: {l2}\n(a)")
print("Length of first list: ",len(l1))
print("Length of second list: ",len(l2))
if len(l1)==len(l2):
	print("Both lists are of same length")
else:
	print("Both lists are not of same length")
sum1=0
sum2=0
for i in l1:
	sum1+=i
for i in l2:
	sum2+=i
print("(b)\nSum of elements of first list: ",sum1)
print("Sum of elements of second list: ",sum2)
if sum1==sum2:
	print("The sum of elements of both the lists are equal")
else:
	print("The sum of elements of both the lists are not equal")
bothlist=[]
for i in l1:
	if i in l2:
		bothlist.append(i)
print("(c)")
if bothlist:
	print("The value occurs in both the lists are:")
	for i in bothlist:
		print (i)
else:
	print("There is no value occurs in both the lists")
