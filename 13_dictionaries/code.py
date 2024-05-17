friend_ages = {
    "Rolf": 24,
    "Anne": 21,
    "Diana": 18
}

friend_ages["Bob"] = 20
friend_ages["Anne"] = 23

print(friend_ages["Diana"])
print(friend_ages)

# ----

friends = [
    { "name": "Rolf", "age": 24 },
    { "name": "Anne", "age": 21 },
    { "name": "Diana", "age": 18 },
]

print(friends[0]["name"])

for friend in friends:
    print(friend)

# ----

student_attendance = {
    "Rolf": 96,
    "Bob": 80,
    "Anne": 100
}

for name, attendance in student_attendance.items():
    print(f"{name}: {attendance}%")