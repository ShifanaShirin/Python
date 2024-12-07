str=input("Enter a string which has reoccurence of first character:")
firstchar=str[0]
newstr=firstchar+str[1:].replace(firstchar,'$')
print("New String : ",newstr)
