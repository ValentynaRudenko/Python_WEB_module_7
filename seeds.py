from faker import Faker
from models import Students, Groups, Lecturers, Classess, Marks
from random import randint
from datetime import datetime
from connect_db import session

fake = Faker()

NUMBER_STUDENTS = 30
NUMBER_LECTURERS = 5
NUMBER_GROUPS = 3
NUMBER_CLASSES = 8


if __name__ == '__main__':

    for _ in range(1, NUMBER_GROUPS+1):
        group = Groups(group_name=fake.random_int())
        session.add(group)

    for _ in range(1, NUMBER_STUDENTS+1):
        student = Students(student=fake.name(),
                           group_id=fake.random_int(1, NUMBER_GROUPS))
        session.add(student)

    for _ in range(1, NUMBER_LECTURERS+1):
        lecturer = Lecturers(lecturer=fake.name())
        session.add(lecturer)

    for _ in range(1, NUMBER_CLASSES+1):
        classs = Classess(class_name=fake.word(),
                          lecturer_id=fake.random_int(1, NUMBER_LECTURERS))
        session.add(classs)

    for st in range(1, NUMBER_STUDENTS + 1):
        for cl in range(1, NUMBER_CLASSES + 1):
            for _ in range(randint(1, 2)):
                mark_date = datetime(
                    2023, randint(1, 12), randint(1, 28)).date()
                mark = Marks(mark=fake.random_int(1, 5),
                             date_of=mark_date,
                             student_id=st,
                             class_id=cl)
                session.add(mark)

    session.commit()
