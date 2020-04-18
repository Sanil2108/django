from django.db import models



class Student(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    age = models.IntegerField()

    # One to many relationship
    course = models.ForeignKey('Course', on_delete = models.CASCADE, blank = True)

    # Many to many relationship


class Course(models.Model):
    course_id = models.CharField(max_length = 20, primary_key = True)
    
    # One to many relationship

    # Many to many relationship
    manyStudents = models.ManyToManyField(Student, related_name = 'many_students', blank = True)