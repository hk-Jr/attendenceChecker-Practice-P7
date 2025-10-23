
c_held = int(input("Enter total number of classes held: "))
c_attended = int(input("Enter number of classes attended: "))
attendance = (c_attended / c_held) * 100

print("Classes Held:", c_held)
print("Classes Attended:", c_attended)
print("Attendance:",attendance)

if attendance >= 75:
    print("Status: Eligible for exams")
else:
    print("Status: Not eligible for exams")