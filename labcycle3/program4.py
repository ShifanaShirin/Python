from math import *
squares=[]
ll=int(input("Enter the lower limit:"))
ul=int(input("Enter the upper limit:"))
for i in range(ll,ul):
	for j in range(1,i):
		if sqrt(i)==j:
			squares.append(i)
print("Perfect squares between this limit:",squares)
even=[]
for i in squares:
	square_str=str(i)
	if int(square_str[0])%2==0 and int(square_str[1])%2==0 and int(square_str[2])%2==0 and int(square_str[3])%2==0:
		even.append(int(square_str))
print("Perfect Squares between this limit with all the digits even:",even)
