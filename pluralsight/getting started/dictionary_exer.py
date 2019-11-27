student = {
    "name" : "Mark",
    "student_id" : 15163,
    "feedback" : None
}

all_students = [
    {"name": "Mark", "student_id": "15163"},
    {"name": "Katarina", "student_id":"63112"},
    {"name": "Jessica", "student_id":"30021"}
]

print(student["name"])
print(all_students[2]["name"])
print(student.items())


#print(student["last_name"])

print(student.get("last_name", "Unknown"))



