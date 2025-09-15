from fastapi import APIRouter, Request
from models import *
from fastapi.templating import Jinja2Templates
import os
from pydantic import BaseModel, field_validator
from typing import List
from fastapi.exceptions import HTTPException


student_api = APIRouter()

@student_api.get("/")
async def getAllStudent():
    ### (1) all() ============================= SELECT * FROM "student";
    # students = await Student.all()        # type Queryset(List[] like): [Student(), Student(), Student(), ...]
    # print("students", students)
    # for student in students:
    #     print(student.name, student.stud_num)


    ### (2) filter() ========================== SELECT * FROM "student" WHERE "name" = 'rain';
    # students = await Student.filter(name='rain')      # type Queryset(List[] like)
    # students = await Student.filter(clas_id=14)       # type Queryset
    # print("students", students)
    # for student in students:
    #     print(student.name, student.stud_num)
    

    ### (3) get() ============================= SELECT * FROM "student" WHERE "id" = 6 LIMIT 1;
    # student = await Student.filter(id=6)      # type Queryset
    # print(student[0].name)                    # when only 1 record, filter() still needs to use index [0] to get the object (troublesome)
    # student = await Student.get(id=6)         # type QuerySetSingle(object/model Instance): Student()
    # print(student.name)


    ### (4) fuzzy query ====================== SELECT * FROM "student" WHERE "stud_num" > 2001;
    ## __range: returns records between the two values (inclusive)
    ## __in: returns records matching exactly the value in the list
    # students = await Student.filter(stud_num__gt=2001)                # type Queryset
    # students = await Student.filter(stud_num__range=(1, 10000))       # type Queryset  
    # students = await Student.filter(stud_num__in=[1, 10000])          # type Queryset
    # print("students", students)
    

    ### (5) values() ======================== SELECT "id", "name" FROM "student";
    # students = await Student.all().values()                       # type List[Dict]: [{}, {}, {}, ...]
    # students = await Student.all().values("name", "stud_num")     # type List[]      
    # print("students", students)


    ### (6) One-to-Many relationship & Many-to-Many relationship
    ## One-to-Many: Student -> Class
    alvin = await Student.get(name="alvin")      # type Student(): QuerySetSingle => object instance
    # print(alvin.name)
    # print(alvin.stud_num)
    # print(await alvin.clas)                       # type QuerySet: [Class()]
    # print((await alvin.clas).name)                # Class 101
    # print(await alvin.clas.values("name"))        # {'name': 'Class 101'}

    # students = await Student.all().values("name", "clas_id", "clas__id", "clas__name")     # type List[]
    # print("students", students)                     # double underscore __ to access related table fields

    ## Many-to-Many: Student <-> Course  
    print(await alvin.courses.all().values("name", "teacher__name"))   # type List[]
    students = await Student.all().values("name", "courses__name", "courses__teacher__name")
    return students


@student_api.get("/index.html")
async def getIndexPage(request: Request):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    template_dir = os.path.join(base_dir, "templates")
    templates = Jinja2Templates(directory=template_dir)
    students = await Student.all()      # type Queryset: [Student(), Student(), Student(), ...]
    return templates.TemplateResponse("index.html", {"request": request, "students": students})


class StudentIn(BaseModel):
    name: str
    pwd: str
    stud_num: int
    # One-to-Many relationship with Class
    clas_id: int
    # Many-to-Many relationship with Course
    courses: List[int] = []

    @field_validator("name")
    def name_must_alphabetic(cls, value):
        assert value.isalpha(), "Name must be alphabetic"
        return value
    
    @field_validator("stud_num")
    def stud_num_validate(cls, value):
        assert value > 1000 and value < 10000, "Student number must be between 1000 and 10000"
        return value

@student_api.post("/")
async def addStudent(student_in: StudentIn):
    ### Add to database
    ## Method 1: Create instance and save
    # student = Student(name=student_in.name, pwd=student_in.pwd, stud_num=student_in.stud_num, clas_id=student_in.clas_id)
    # await student.save()
    ## Method 2: Use create() method
    student = await Student.create(name=student_in.name, pwd=student_in.pwd, stud_num=student_in.stud_num, clas_id=student_in.clas_id)

    ## Add Many-to-Many relationships
    ## student_in.courses      List: [7, 8, ...]
    choose_courses = await Course.filter(id__in=student_in.courses)    # type Queryset: [Course(), Course(), ...]
    await student.courses.add(*choose_courses)      # .add() only accepts Object instances, so use * to unpack the List[...]
    return {"Post": "Add a new student"}


@student_api.put("/{student_id}")
async def updateStudent(student_id: int, student_in: StudentIn):
    data = student_in.model_dump()      # .dict() in class "BaseModel" is deprecated, use .model_dump() instead
    print("data", data)
    courses = data.pop("courses")       # Remove "courses" from data dictionary, as it's a Many-to-Many relationship
    ## NEW: courses = List: [7, 8, ...], data = {'name': 'xx', 'pwd': 'xx', 'stud_num': xx, 'clas_id': xx}

    await Student.filter(id=student_id).update(**data)      # ** to unpack the dictionary

    edit_student = await Student.get(id=student_id)         # Student()
    choose_courses = await Course.filter(id__in=courses)    # __in accepts a list, returns Queryset: [Course(), Course(), ...]
    await edit_student.courses.clear()                      # Clear existing Many-to-Many relationships
    await edit_student.courses.add(*choose_courses)

    return edit_student


@student_api.delete("/{student_id}")
async def deleteStudent(student_id: int):
    delete_count = await Student.filter(id=student_id).delete()
    if not delete_count:
        raise HTTPException(status_code=404, detail=f"Student ID {student_id} not found")
    
    return {}


@student_api.get("/{student_id}")
async def getStudentById(student_id: int):
    student = await Student.get(id=student_id)   # type QuerySetSingle: Student()

    return student