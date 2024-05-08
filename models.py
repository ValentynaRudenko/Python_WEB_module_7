from sqlalchemy import Integer, \
    String, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Lecturers(Base):
    __tablename__ = "lecturers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    lecturer: Mapped[str] = mapped_column(String(30))
    user: Mapped["Classess"] = relationship(back_populates="lecturer")


class Classess(Base):
    __tablename__ = "classess"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    class_name: Mapped[str] = mapped_column(String, nullable=False)
    lecturer_id: Mapped[int] = mapped_column("lecturer_id", Integer,
                                             ForeignKey("lecturers.id"))
    lecturer: Mapped["Lecturers"] = relationship(back_populates="user")
    mark: Mapped["Marks"] = relationship(back_populates="classs")


class Groups(Base):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    group_name: Mapped[str] = mapped_column(String, nullable=False)
    student: Mapped["Students"] = relationship(back_populates="group")


class Students(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    student: Mapped[str] = mapped_column(String, nullable=False)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    group: Mapped["Groups"] = relationship(back_populates="student")
    mark: Mapped["Marks"] = relationship(back_populates="student")


class Marks(Base):
    __tablename__ = "marks"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    mark: Mapped[int] = mapped_column(Integer)
    date_of: Mapped[datetime] = mapped_column(DateTime)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    class_id: Mapped[int] = mapped_column(ForeignKey("classess.id"))
    student: Mapped["Students"] = relationship(back_populates="mark")
    classs: Mapped["Classess"] = relationship(back_populates="mark")


# Base.metadata.create_all(engine)
# Base.metadata.bind = engine
