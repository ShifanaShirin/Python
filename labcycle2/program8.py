colors=input("Enter the name of colours seperated by commas:")
colors=colors.split(',')
color_list=[]
for i in colors:
	color_list.append(i.strip())
print("The list of colours is:",color_list)
if color_list:
	print("First Colour:",color_list[0])
	print("Last Color:",color_list[-1])
else:
	print("No colors entered")
