students = []

for i in range(3):
	name = input("Enter your name: ")
	while True:
		gender = input(f"Your Gender (m/f): ").lower()
		if gender in ("m", "f"):
			break
		print("Invalid input!")
	score = float(input("Enter your score: "))

	student = {
	"name": name,
	"gender": gender,
	"score": score
	}

	students.append(student)

print(students)


