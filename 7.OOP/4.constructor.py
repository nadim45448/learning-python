class Student:
    id=""
    cgpa=""

    # declare constructor
    def __init__(self,id,cgpa):
        self.id=id
        self.cgpa=cgpa
    def show(self):
        print(f'id:{self.id}, cgpa:{self.cgpa}')


x=Student("12345",3.95)
x.show()