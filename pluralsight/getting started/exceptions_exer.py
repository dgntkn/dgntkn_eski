student = {
    "name" : "Mark",
    "student_id" : 15163,
    "feedback" : None
}

student["last_name"] = "Kowalski"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding last_name")
except TypeError as error:
    print("it can not be added")
    print(error)

print("This code executes")