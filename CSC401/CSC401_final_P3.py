'''
CSC 401: Final Exam (take home)
Problem 3: Grading - 25pts
'''

def grades():
    for student, grade in classlst.items():
        print("Student {} got a {}".format(student,classlst[student]))
        
student = input("Student: ") 
grade = input("Grade: ")
classlst = {}
    

while student != '':
    classlst[student] = grade  
    student = input("Student: ") 

    if student not in classlst:
        grade = input("Grade: ")  
        
    if student in classlst:
        print("You already assigned a grade of {} to {}".format(classlst[student], student))
        ask = input("Do you want to change that (y/n)? ")
        if ask == "y":
            grade = input("Grade: ")
            classlst[student] = grade
        else:
            student = input("Student: ")
            if student == '':
               print(grades())
            else:
               grade = input("Grade: ")

    if student == '' or grade == '':
        print(grades())
        
        
        

           

      
 
