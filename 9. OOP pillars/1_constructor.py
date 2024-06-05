class School:
    def __init__(self, name, address, principal='') -> None:
        self.name=name
        self.address=address
        self.principal=principal
        self.grade=[]
        pass

    def add_grade(self, name, teacher):
        new_grade=Grade(name, teacher) #access Grade class
        self.grade.append(new_grade)
        pass
    

class Grade:
    def __init__(self, name, teacher) -> None:
        self.students=[]
        self.name=name
        self.teacher=teacher
        pass

    def __repr__(self) -> str:
        return f'{self.name}, teacher:{self.teacher}'
        pass

    

aiub=School('AIUB Academy', 'Kuratoli', 'nadia')
aiub.add_grade('class 4', ' Nadim')
aiub.add_grade('class 5', ' Rahim')
print(aiub.grade)