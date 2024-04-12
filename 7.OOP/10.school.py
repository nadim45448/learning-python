class Student:
    def __init__(self, name, age, id): 
        self.name=name
        self.age=age
        self.id=id

class Course:
    def __init__(self, name, faculty):
        self.name=name
        self.faculty=faculty

class Teacher:
    def __init__(self, name, course):
        self.name=name
        self.course=course

class School:
    def __init__(self,name, faculties,courses, students):
        self.name=name
        self.fcaulties=faculties
        self.courses=courses
        self.students=students

    def get_students(self):
        for student in self.students:
            print(student.name)


school_name='Galaxy High School' 

ds_coourse=Course('Data Structure','Einstein')
algo_course=Course('Algorithm','Edison')

teacher1=Teacher('Einstein',ds_coourse)
teacher2=Teacher('Edison',algo_course)

student1=Student('jodu',19,45)
student2=Student('modu',29,69)
student3=Student('kodu',28,55)

teachers=[teacher1,teacher2]
courses=[ds_coourse,algo_course]
students=[student1,student2,student3]

my_scholl=School(school_name,teachers,courses,students)

print(my_scholl.students)
my_scholl.get_students()

        
        
        