words=input("Enter a list of words seperated by spaces:")
a=words.split()
l=[]
for i in a:
	l.append(i.strip())
print("The list of words is:",l)
max_len=-1
long=[]
for i in l:
	if len(i)>max_len:
		max_len=len(i)
print("Length of longest word: ",max_len)
