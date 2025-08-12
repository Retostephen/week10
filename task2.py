numbers = [12, 75, 150, 180, 145, 525, 50]
count = len(numbers) -1
for number in range(len(numbers)):
	print(numbers[count])
	count -= 1

'''
length = len(numbers) -1
for number in range(length //2):
	num = numbers[number]
	numbers[number] = numbers[length -1 -number]
	numbers[length -1 -number] = num
	print(numbers)
'''
	
