numbers = [12, 75, 150, 180, 145, 525, 50]
#Tak to reverse the list without using method only for loop
'''
count = len(numbers) -1
for number in range(len(numbers)):
	print(numbers[count])
	count -= 1
'''
'''
length = len(numbers) -1
for number in range(length //2):
	num = numbers[number]
	numbers[number] = numbers[length -1 -number]
	numbers[length -1 -number] = num
	print(numbers)
'''
#Task to find the highest value in a list without using method
largest = numbers[0]
for num in numbers:
	if num > largest:
		largest = num
print(largest)

