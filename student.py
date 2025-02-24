from human import Human
from group import Group

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}, Record Book: {self.record_book}'

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)  # Порівняння через рядок
        return False

    def __hash__(self):
        return hash(str(self))

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
gr = Group('PD0')
gr.add_student(st1)
assert gr.find_student('Jobs') == st1
print(gr)