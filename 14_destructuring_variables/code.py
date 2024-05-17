tuple = 5, 11
x, y = tuple

print(x, y)

# ----

student_attendance = {
    "Rolf": 96,
    "Bob": 80,
    "Anne": 100
}

print(list(student_attendance.items()))

# for name, attendance in student_attendance.items():
#     print(f"{name}: {attendance}%")

# ----

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, proffesion in people:
    print(f"Name: {name}, Age: {age}, Proffesion: {proffesion}")

# ----

person = ("Bob", 42, "Mechanic")

name, _, proffesion = person

print(name, proffesion)

# ----

head, *tail = [1, 2, 3, 4, 5] # head = 1 | tail = [2, 3, 4, 5]
# *head, tail = [1, 2, 3, 4, 5] # head = [1, 2, 3, 4] | tail = 5

print(head)
print(tail)