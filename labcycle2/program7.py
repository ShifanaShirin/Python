a=int(input("Enter the number of colours to be inserted in first list of  colours:"))
colour_list1=[]
for i in range(a):
        colour_list1.append(input("Enter the  name of a colour:"))
print("The first list of colours is:",colour_list1)
b=int(input("Enter the number of colours to be inserted in second list of  colours:"))
colour_list2=[]
for i in range(b):
        colour_list2.append(input("Enter the  name of a colour:"))
print("The second list of colours is:",colour_list2)
result_list=[]
for i in colour_list1:
        if i not in colour_list2:
                result_list.append(i)
print("The colors from first list not contained in second list are:",result_list)
