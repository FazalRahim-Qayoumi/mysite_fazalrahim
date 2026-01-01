from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Class Table
# ---------------------------


class Class(models.Model):
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=5)
    class_teacher = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.section}"


# ---------------------------
# Parent Table
# ---------------------------
class Parent(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()

    def __str__(self):
        return self.name


# ---------------------------
# Teacher Table
# ---------------------------
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


# ---------------------------
# Subject Table
# ---------------------------
class Subject(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, related_name='subjects', null=True)

    def __str__(self):
        return f"{self.name} ({self.code})"


# ---------------------------
# Student Table
# ---------------------------
class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE ,related_name='students')
    address = models.CharField(max_length=30)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.name} ({self.roll_no})"


# ---------------------------
# Marks Table
# ---------------------------
class Marks(models.Model):
    EXAM_CHOICES = [
        ('MID', 'Mid Term'),
        ('FINAL', 'Final Exam'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE ,related_name='mark')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,related_name='mark')
    marks_obtained = models.FloatField()
    exam_type = models.CharField(max_length=10, choices=EXAM_CHOICES)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} ({self.exam_type})"


# ---------------------------
# Attendance Table
# ---------------------------
class Attendance(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='attendace')
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student.name} - {self.date} ({self.get_status_display()})"
    
class Staff(models.Model):
    prancipal=models.CharField(max_length=100)
    vice_prancipal=models.CharField(max_length=100)
    School_secretary=models.CharField(max_length=100)
    Accountant=models.CharField(max_length=100)
    Subject_teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='staff',blank=True)
    librarian=models.CharField(max_length=100)
    IT_technation=models.CharField(max_length=100)
    guard=models.CharField(max_length=100)
    cleaner=models.CharField(max_length=100)
    

    # fees section 
from django.db import models
from django.utils import timezone

class Fees(models.Model):
    FEES_STATUS = [
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
        ('partial', 'Partial'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fees')
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='class_fees')
    total_fees = models.PositiveIntegerField(default=0)
    paid_amount = models.PositiveIntegerField(default=0)
    balance_amount = models.PositiveIntegerField(default=0)
    payment_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=FEES_STATUS, default='unpaid')

    def save(self, *args, **kwargs):
        self.balance_amount = self.total_fees - self.paid_amount
        if self.paid_amount >= self.total_fees:
            self.status = 'paid'
        elif self.paid_amount == 0:
            self.status = 'unpaid'
        else:
            self.status = 'partial'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - {self.status} ({self.balance_amount})"



   
    # end of fees section



# new one profile 
from django.db import models
from django.contrib.auth.models import User
# models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings  # <--- import settings


    
    # other fields

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('staff', 'Staff'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/', default='default.jpg')
    bio = models.TextField(blank=True, null=True)  # optional

    def __str__(self):
        return f"{self.user.username} Profile"


# Signal to create/update Profile automatically
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


