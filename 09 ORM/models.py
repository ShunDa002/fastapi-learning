from tortoise.models import Model
from tortoise import fields


class Student(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="Student Name")
    pwd = fields.CharField(max_length=32, description="Student Password")
    stud_num = fields.IntField(description="Student Number")

    # One-to-Many relationship with Class
    clas = fields.ForeignKeyField("models.Clas", related_name="students")
    # Many-to-Many relationship with Course
    courses = fields.ManyToManyField("models.Course", related_name="students")


class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="Course Name")
    teacher = fields.ForeignKeyField("models.Teacher", related_name="courses")


class Clas(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="Class Name")


class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32, description="Teacher Name")
    pwd = fields.CharField(max_length=32, description="Teacher Password")
    teac_num = fields.IntField(description="Teacher Number")
