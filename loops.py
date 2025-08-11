'''
#numbers = [1, 2, 3, 4, 5]

#for number in numbers:
#	print(number)

#for i in range(1, 101, 3):
#	print(f"Number {i}")
names = ["Tom", "Jerry", "Mimi", "Val", "John"]
#for i in range(len(names)):
#	print(i)



#user_input = input("Enter a name: ")
for name in names:
	user_input = input("Enter a name: ")
	if user_input == name:
		print("VIP")
	else:
		print("Regular")
'''

for i in range (1, 101):
	total = i * i
	print(f"{i} * {i} = {total}")
		
