'''
#numbers = [1, 2, 3, 4, 5]

#for number in numbers:
#	print(number)

#for i in range(1, 101, 3):
#	print(f"Number {i}")
names = ["Tom", "Jerry", "Mimi", "Val", "John"]
#for i in range(len(names)):
#	print(i)
'''

'''
#user_input = input("Enter a name: ")
for name in names:
	user_input = input("Enter a name: ")
	if user_input == name:
		print("VIP")
	else:
		print("Regular")
'''
'''
for i in range (1, 101):
	total = i * i
	print(f"{i} * {i} = {total}")
'''

names = ["Tom", "Jerry", "Mimi", "Val"]

user_name = input("UserName\n>>>")
flag = False
for name in names:
if user_name == name:
		flag = True
		break
if flag == True:
	print("VIP")
else:
	print("Regular")	
