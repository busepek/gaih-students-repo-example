n = 5  # number of students to be calculated
students = []  # students names and surnames
grades = []  # students grades
averages = []  # average grades of students
info = {}
weigh = {}

for i in range(n):
    st_name = input("Please write student's name: ")
    st_sname = input("Please write student's surname: ")
    students.append(st_name + " " + st_sname)
    mt_grade = int(input("Please write student's midterm grade: "))
    hw_grade = int(input("Please write student's homework grade: "))
    final_grade = int(input("Please write student's final grade: "))
    grades.append([mt_grade, hw_grade, final_grade])
    averages.append(int((mt_grade + hw_grade + final_grade) / 3))
    zip_lists1 = zip(students, grades)
    info = dict(zip_lists1)
    zip_lists2 = zip(students, averages)
    weigh = dict(zip_lists2)

average_sort = sorted(averages)
max_grade = averages.index(average_sort[n - 1])
max_student = students[max_grade]

print("Students: ", students)
print("Grades: ", grades)
print("Infos: ", info)
print("Grades Weigh of Students: ", weigh)
# print("Sorted Grades Weigh", average_sort)
print("Congratulations", max_student)
