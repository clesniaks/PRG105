outfile = open("grades.txt", "w")
num_students = int(input("How many students do you need to enter grades for?:"))
student_grades = [] * num_students
for i in range(num_students):
    line = [input("Enter the name of student " + str(i) + ": "), input("Enter the grade of the student: ")]
    student_grades.append(line)


for line in student_grades:
    lineout = "'" + line[0] + "', '" + line[1] + "'\n"
    outfile.writelines(lineout)
outfile.close()
