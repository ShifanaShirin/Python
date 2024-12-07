numbers=input("Enter a list of integers seperated by spaces:")
a=numbers.split()
l=[]
for i in a:
        l.append(int(i))
print("List:",l)
newlist=[]
for i in l:
        if i%2!=0:
                newlist.append(i)
print("New List:",newlist)
