n=int(input("Enter the number of elements:"))
lst=[]
for i in range(n):
        a=int(input("Enter the element:"))
        lst.append(a)
mult=list(filter(lambda x:x%3==0,lst))
print("Multiples of 3:")
print(mult)
