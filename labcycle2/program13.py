line=input("Enter a line of text:").split()
l=[]
for i in line:
	i.lower()
	l.append(i)
print("The list of words in this line of text is:",l)
d=dict()
for i in l:
	if i in d:
		d[i]=d[i]+1
	else:
		d[i]=1
for i in d:
	print(f"The number of occurence of '{i}' : {d[i]}")
