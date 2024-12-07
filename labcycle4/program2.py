def addition(a,b):
	return a+b
def subtraction(a,b):
	return a-b
def multiplication(a,b):
	return a*b
def division(a,b):
	return a/b
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
while True:
	print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
	c=input("Enter your choice:")
	if c=='5':
		break;
	elif c=='1':
		print(f"{a} + {b} = {addition(a,b)}\n")
	elif c=='2':
		print(f"{a} - {b} = {subtraction(a,b)}\n")
	elif c=='3':
		print(f"{a} * {b} = {multiplication(a,b)}\n")
	elif c=='4':
		print(f"{a} / {b} = {division(a,b)}\n")
	else:
		print("Invalid Choice!!\n")
