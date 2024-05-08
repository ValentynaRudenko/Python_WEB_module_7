from sqlalchemy import func
from models import Students, Groups, Lecturers, Classess, Marks
from connect_db import session


def select_1():
    q = session.query(
        Students.id,
        Students.student,
        func.round(func.avg(Marks.mark), 2).label('avg_mark')
        )\
        .select_from(Marks)\
        .join(Students)\
        .group_by(Students.id)\
        .order_by(func.avg(Marks.mark).desc()).limit(5).all()
    return q


def select_2():
    q = session.query(
        Students.id,
        Students.student,
        Classess.class_name,
        func.round(func.avg(Marks.mark), 2).label('avg_mark')
        )\
        .select_from(Marks)\
        .join(Students)\
        .join(Classess)\
        .filter(Classess.id == 2)\
        .group_by(Students.id)\
        .order_by(func.avg(Marks.mark).desc()).limit(5).all()
    return q


def select_3():
    q = session.query(
        Groups.group_name,
        Classess.class_name,
        func.round(func.avg(Marks.mark), 2)
        )\
        .select_from(Marks)\
        .join(Students)\
        .join(Groups)\
        .join(Classess)\
        .filter(Classess.id == 3)\
        .group_by(Groups.id)\
        .order_by(func.avg(Marks.mark).desc()).all()
    return q


def select_4():
    q = session.query(
        func.round(func.avg(Marks.mark), 2)
        )\
        .select_from(Marks)\
        .all()
    return q


def select_5():
    q = session.query(
        Lecturers.lecturer,
        Classess.class_name,
        )\
        .select_from(Classess)\
        .join(Lecturers)\
        .filter(Lecturers.id == 2)\
        .all()
    return q


def select_6():
    q = session.query(
        Groups.group_name,
        Students.student
        )\
        .select_from(Students)\
        .join(Groups)\
        .filter(Groups.id == 1)\
        .all()
    return q


def select_7():
    q = session.query(
        Groups.group_name,
        Classess.class_name,
        Students.student,
        Marks.mark
        )\
        .select_from(Marks)\
        .join(Students)\
        .join(Classess)\
        .join(Groups)\
        .filter(Groups.id == 1, Classess.id == 3)\
        .all()
    return q


def select_8():
    q = session.query(
        Lecturers.lecturer,
        Classess.class_name,
        func.round(func.avg(Marks.mark), 2)
        )\
        .select_from(Lecturers)\
        .join(Classess)\
        .join(Marks)\
        .filter(Lecturers.id == 1)\
        .all()
    return q


def select_9():
    q = session.query(
        Classess.class_name,
        Students.student,
        )\
        .select_from(Students)\
        .join(Marks)\
        .join(Classess)\
        .filter(Students.id == 12)\
        .all()
    return q


def select_10():
    q = session.query(
        Lecturers.lecturer,
        Students.student,
        Classess.class_name,
        )\
        .select_from(Students)\
        .join(Marks)\
        .join(Classess)\
        .join(Lecturers)\
        .filter(Students.id == 1, Lecturers.id == 3)\
        .all()
    return q


if __name__ == "__main__":
    print("Select_1: ", select_1())
    print("Select_2: ", select_2())
    print("Select_3: ", select_3())
    print("Select_4: ", select_4())
    print("Select_5: ", select_5())
    print("Select_6: ", select_6())
    print("Select_7: ", select_7())
    print("Select_8: ", select_8())
    print("Select_9: ", select_9())
    print("Select_10: ", select_10())
