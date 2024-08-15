from sqlalchemy import Column, Integer, Float, String, Date, Boolean, ForeignKey, Enum, func, distinct
from sqlalchemy.orm import relationship
from StudentManage import db
from datetime import datetime
from flask_login import UserMixin


if _name_ == '_main_':
    db.drop_all()
    db.create_all()

    # Tao subject
    subject1 = Subject(name='Math')
    subject2 = Subject(name='History')
    db.session.add_all([subject1, subject2])
    db.session.commit()

    # Tao account
    admin = Account(username='admin',
                    password=hashlib.md5('123'.strip().encode("utf-8")).hexdigest(),
                    firstname='admin',
                    lastname='admin',
                    admin=True)
    gv = Account(username='gv',
                    password=hashlib.md5('123'.strip().encode("utf-8")).hexdigest(),
                    firstname='gv',
                    lastname='gv')
    db.session.add_all([admin, gv])
    db.session.commit()

    # Tao class

    class10 = Class(course=2, grade='10', name='Lop 10')
    class1 = Class(course=1, grade='11', name='Lop 11')
    class2 = Class(course=2, grade='12', name='Lop 12')
    db.session.add_all([class10, class1, class2])
    db.session.commit()

    # Tao teach
    teach1 = Teach(teacher_id=gv.id, class_id=class1.id)
    teach2 = Teach(teacher_id=gv.id, class_id=class2.id)
    teach3 = Teach(teacher_id=gv.id, class_id=class10.id)
    db.session.add_all([teach1, teach2, teach3])
    db.session.commit()

    # Tao Student them vao Class
    student1 = Student(firstname='Thanh', lastname='Dat',
                       fullname='Thanh Dat', male='Male',
                       class_id=class1.id)
    student2 = Student(firstname='Sieu', lastname='Nhan',
                       fullname='Sieu Nhan', male='Male',
                       class_id=class1.id)
    student3 = Student(firstname='Phu', lastname='Nu',
                       fullname='Phu Nu', male='Female',
                       class_id=class1.id)
    student4 = Student(firstname='Nguyen', lastname='A',
                       fullname='Nguyen A', male='Female',
                       class_id=class2.id)
    student5 = Student(firstname='Nguyen', lastname='B',
                       fullname='Nguyen B', male='Female',
                       class_id=class2.id)
    student6 = Student(firstname='Nguyen', lastname='C',
                       fullname='Phu Nu', male='Female',
                       class_id=class10.id)

    db.session.add_all([student1, student2, student3, student4, student5, student6])
    db.session.commit()

    # Tao test
    test1 = Test(name='Kiem tra 1')
    db.session.add_all([test1, ])
    db.session.commit()

    # Tao score
    score1 = Scores(student_id=student1.id,
                   subject_id=subject1.id,
                   test_id=test1.id,
                   scores=8.2,
                   semester='1')
    score2 = Scores(student_id=student1.id,
                    subject_id=subject1.id,
                    test_id=test1.id,
                    scores=5,
                    semester='1')
    score3 = Scores(student_id=student1.id,
                    subject_id=subject1.id,
                    test_id=test1.id,
                    scores=7,semester='2')

    score4 = Scores(student_id=student2.id,
                    subject_id=subject1.id,
                    test_id=test1.id,
                    scores=1,
                    semester='1')
    score5 = Scores(student_id=student2.id,
                    subject_id=subject1.id,
                    test_id=test1.id,
                    scores=2,
                    semester='1')
    db.session.add_all([score1, score2, score3, score4, score5])
    db.session.commit()

    # Them rule
    rule1 = Rule(course=1, name='MinAge', value='17')
    rule2 = Rule(course=1, name='MaxAge', value='20')
    rule3 = Rule(course=1, name='MaxPopulation', value='40')
    db.session.add_all([rule1, rule2, rule3])
    db.session.commit()
