student_names =  ["james", "katarina", "jessica", "mark", "bort", "frank grimes", "max power"]
print(student_names)

for name in student_names:
    print (f"Student name is {name}")


x = 0
for index in range(5, 10, 2):
    x += 10
    print(f"the value of x is {x}")


for name in student_names:
    if name == "bort":
        continue
    if name == "frank grimes":
        print("found him! " + name)
        break
    print("curently testing " + name)