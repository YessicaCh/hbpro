from django.db import models

# Create your models here.
# users/models.py
from django.contrib.auth.models import AbstractUser, UserManager

class User(UserManager):
    pass

#new
class HbproUser(AbstractUser):
    id_user = models.AutoField(primary_key=True)
    nick_name = models.CharField(max_length=50, blank='False', null='False',default='')
    name = models.CharField(max_length=50,default='')
    last_name = models.CharField(max_length=50,default='')
    #password = models.CharField(max_length=100, blank='False',default='')   
    age = models.IntegerField(default=18, blank='False')
    e_mail = models.EmailField(max_length=50, blank='False',default='example@gmail')
    number_phone = models.IntegerField(blank='False', null='True',default=999999999)
    github = models.URLField(max_length=50,default='https://github.com/example')
    Student_Mentor = models.BooleanField(default=True)  # True = Student, False = Mentor
    objects = User()

"""class Student2(User):
    is_working = models.BooleanField(default=False)

    def __str__(self):
        return (self.name)

class Mentor(User):
    is_mentorizing = models.BooleanField(default=False)
    
    def __str__(self):
        return (self.name)

class Program(models.Model):
    year = models.SmallIntegerField()
    title = models.CharField(max_length=50)

    def __str__(self):
        return (self.title)

class Students_Mentor(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)  # One to many = foreign
    studentA = models.ForeignKey(Student2, null=True, related_name='studentA', on_delete=models.CASCADE)
    studentB = models.ForeignKey(Student2, null=True, related_name='studentB', on_delete=models.CASCADE)    
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

class Course(models.Model):
    name = models.CharField(max_length=50)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name)

class Courses_Student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student2 = models.ForeignKey(Student2, on_delete=models.CASCADE)
    percentage = models.IntegerField()

    def __str__(self):
        return (self._check_single_primary_key)  """
