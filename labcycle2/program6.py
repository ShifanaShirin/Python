str1=input("Enter the first name of first person:")
str2=input("Enter the first name of second person:")
str3=input("Enter the first name of third person:")
str4=input("Enter the first name of fourth person:")
str5=input("Enter the first name of fifth person:")
l=[str1,str2,str3,str4,str5]
count=0
for i in l:
        for j in i:
                if j=="a":
                        count+=1
print("The occurence of 'a' within the list of these first names is ",count)
