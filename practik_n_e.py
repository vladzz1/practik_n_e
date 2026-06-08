student = {
    "name": "іван марко",
    "age": 18,
    "grade": 95
}

print(student)

print(student.get("name"))
print(student["name"])

student["gmail"] = "ivan@gmail.com"

print(student)

del student["grade"]
print(student)

for key in student:
    print(f"{key}: {student[key]}")

mysquart = lambda x : x * x

print(mysquart(5))

def square(num):
    return num * num

print(square(5))

students = [
    {"name": "Bob", "age": 35},
    {"name": "Alice", "age": 18},
    {"name": "Bist", "age": 35}
]

# students.sort(key=lambda x: x["age"])
# print(students)

sorted_stud = sorted(students, key=lambda student: student["age"])
print(sorted_stud)

print(type(students[0]))

myTuple = (23, 12, 24)
print(type(myTuple))
print(myTuple[1])

try:
    myTuple[0] = 18
except TypeError as x:
    print("Хюстон у нас проблеми", x)

print(f"Кількість елементів у кортежі: {len(myTuple)}")

for item in myTuple:
    print("Елементи списку:", item)

# i = 0
# while(i < len(myTuple)):
#     print(f"myTuple[{i}]")