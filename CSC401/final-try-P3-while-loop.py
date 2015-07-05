'''
CSC 401: Final Exam (take home)
Problem 3: Grading - 25pts
'''

def grades():
    for student, grade in classlst.items():
        print("Student {} got a {}".format(student,grade))
        
        


student = input("Student: ") # initial
grade = input("Grade: ")
classlst = {}
    

while student != '':
    classlst[student] = grade  # adds the student key and grade value to a dictionary
    student = input("Student: ") # new entry

    if student not in classlst:
        grade = input("Grade: ")  # new entry
        
    if student in classlst:
        print("You already assigned a grade of {} to {}".format(classlst[student], student))
        ask = input("Do you want to change that (y/n)? ")
        if ask == "y":
            gradeNew = input("Grade: ")
            classlst[student] = gradeNew
        else:
            student = input("Student: ")
            if student == '':
               print(grades())
            else:
               grade = input("Grade: ")


        
        
        

           

      
 
