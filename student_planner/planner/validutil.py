from planner.models import Planner, Student
import json
import os

def validateMajor(planner: Planner, student: Student):
    majors = [student.major_one, student.major_two]
    minors = [student.minor_one, student.minor_two]
    for i, major in enumerate(majors):
        if major is not None:
            majors[i] = major.id
    for i, minor in enumerate(minors):
        if minor is not None:
            minors[i] = minor.id
    courses = pull_courses(planner)
    validator = {}
    with open('planner/degree_audit.json') as f:
        data = json.load(f)
        for major in majors:
            if major is not None:
                unfulfilled, remaining = check_specific(courses, data['Majors'][major]['specific'])
                validator[major] = {'unfulfilled': unfulfilled}   
                unfulfilled, remaining = check_additional(remaining, data['Majors'][major]['additional'])           
    

    return validator


def check_specific(courses: dict, spec: dict):
    for item in courses.copy():
        if item in spec:
            courses.remove(item)
            spec.remove(item)
    
    return spec, courses
   

def check_additional(courses: dict, add: dict):
    for add_ in add:
        parse_additional(add_)
    return 1, 2


def parse_additional(add: str):
    num, level = add.split('.')
    print(f'num: {num}, level: {level}')


def pull_courses(planner: Planner):
    planner.semesters = [
                ('fall_one', planner.fall_one),
                ('spring_one', planner.spring_one),
                ('fall_two', planner.fall_two),
                ('spring_two', planner.spring_two),
                ('fall_three', planner.fall_three),
                ('spring_three', planner.spring_three),
                ('fall_four', planner.fall_four),
                ('spring_four', planner.spring_four),
            ]
    return [course.id for semester in planner.semesters for course in semester[1].courses.all()]
