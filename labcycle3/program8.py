from math import *
n=int(input("Enter the upper limit:"))
l=[]
for i in range(1, n + 1):
    a = str(i)
    s = 0
    for j in a:
        b = int(j)
        s += b
    l.append(s)
print("\nSum of digits of numbers within this limit:",l)
prime=[]
for i in l:
    is_prime=True
    for j in range(2,int(sqrt(i))+1):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        if i!=1:
            prime.append(i)
print("\nSum of digits of numbers within this limit where the sum is prime number are:",prime)
