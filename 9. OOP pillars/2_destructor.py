import time
class School:
    def __init__(self, name, address, principla='') -> None:
       self.name=name
       self.address=address
       self.principal=principla
       self.grade=[]
       pass

    def add_grade(self, name, teacher):
        new_grade=Grade(name, teacher)
        self.grade.append(new_grade)
        pass

    def remove_grade(self, name):
        idx=0
        for i, grade in enumerate(self.grade):
            if grade.name==name:
                idx=i
            else:
                print('not found')
        del self.grade[idx]


class Grade:
    def __init__(self, name, teacher) -> None:
        self.name=name
        self.teacher=teacher
        pass

    def __repr__(self) -> str:
        return f'{self.name}, teacher:{self.teacher}'
        pass
    def __del__(self):
        print(f'deleting {self.name} with teacher {self.teacher}')

aiub=School('AIUB Academy', 'Kuratoli', 'nadia')
aiub.add_grade('class 4', 'nadim')
aiub.add_grade('class 5', 'Rahim')
# print(aiub.grade)
aiub.add_grade('class 6','karim')
print(aiub.grade)

print()
aiub.remove_grade('class 6')
print(aiub.grade)
print('My code running is done')
time.sleep(10)
print(aiub.grade)



    