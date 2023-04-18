import matplotlib.pyplot as plt

student_names=["Adit","Rahul","Aryan","Mohan","John"]
student_marks=[45,25,37,23,49]

marks_percentage=[45/50*100,25/50*100,37/50*100,23/50*100,49/50*100]

def line_chart_students_marks():
    plt.plot(student_names,student_marks)
    plt.title("Student Marks Graph ")

    plt.xlabel("Student Names")
    plt.ylabel("Students Marks")
    plt.xlim(xmin=0, xmax=8)
    plt.ylim(ymin=1,ymax=50)
    plt.grid(True)

    plt.show()

line_chart_students_marks()




