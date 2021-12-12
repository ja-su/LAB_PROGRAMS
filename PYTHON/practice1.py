students = []

for i in range(3):
    profile = []
    for i in range(1):
        name = input("Enter the name: ")
        score = int(input("Enter the score: "))
        profile.append(name)
        profile.append(score)
    students.append(profile)

students.sort()
print(students)
