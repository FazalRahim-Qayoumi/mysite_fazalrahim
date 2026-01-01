from calendar import c
# from dataclasses import fields
from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from xml.dom.minidom import Attr
from django import forms
from django.forms import ModelForm
# from . models import student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Teacher,Parent,Subject,Student,Marks,Attendance,Staff,Fees,Class
class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'section', 'class_teacher']
        labels = {
            'name': 'Class Name',
            'section': 'Section',
            'class_teacher': 'Class Teacher',
        }

    def __init__(self, *args, **kwargs):
        super(ClassForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control mb-2',
                'placeholder': field.label
            })

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'subject', 'phone', 'email']
        labels = {
            'name': 'Full Name',
            'subject': 'Subject',
            'phone': 'Phone Number',
            'email': 'Email Address',
        }

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control mb-2',
                'placeholder': field.label
            })



class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['name', 'phone', 'email', 'address']
        labels = {
            'name': 'Full Name',
            'phone': 'Phone Number',
            'email': 'Email Address',
            'address': 'Home Address',
        }

    def __init__(self, *args, **kwargs):
        super(ParentForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control mb-2',
                'placeholder': field.label
            })




class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'code', 'teacher']
        labels = {
            'name': 'Subject Name',
            'code': 'Subject Code',
            'teacher': 'Teacher',
        }

    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control mb-2',
                'placeholder': field.label
            })

# student section 
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_no', 'date_of_birth', 'gender', 'student_class', 'address', 'parent']
        labels = {
            'name': 'Full Name',
            'roll_no': 'Roll Number',
            'date_of_birth': 'Date of Birth',
            'gender': 'Gender',
            'student_class': 'Class',
            'address': 'Address',
            'parent': 'Parent',
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control mb-2',
                'placeholder': field.label
            })
        # For date field, add type="date"
        self.fields['date_of_birth'].widget.attrs.update({'type': 'date'})

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'subject', 'marks_obtained', 'exam_type']
        labels = {
            'student': 'Student',
            'subject': 'Subject',
            'marks_obtained': 'Marks Obtained',
            'exam_type': 'Exam Type',
        }

    def __init__(self, *args, **kwargs):
        super(MarksForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control mb-2',
                'placeholder': field.label
            })


# attendancy section 

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']
        labels = {
            'student': 'Student',
            'date': 'Date',
            'status': 'Status',
        }

    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control mb-2',
                'placeholder': field.label
            })
        self.fields['date'].widget.attrs.update({'type': 'date'})

#  staff section 


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['prancipal', 'vice_prancipal', 'School_secretary', 'Accountant', 'Subject_teacher', 'librarian', 'IT_technation', 'guard', 'cleaner']
        labels = {
            'prancipal': 'Principal',
            'vice_prancipal': 'Vice Principal',
            'School_secretary': 'School Secretary',
            'Accountant': 'Accountant',
            'Subject_teacher': 'Subject Teacher',
            'librarian': 'Librarian',
            'IT_technation': 'IT Technician',
            'guard': 'Guard',
            'cleaner': 'Cleaner',
        }

    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control mb-2',
                'placeholder': field.label
            })

# fees section 
from django import forms
from .models import Fees

class FeesForm(forms.ModelForm):
    class Meta:
        model = Fees
        fields = ['student', 'student_class', 'total_fees', 'paid_amount']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'student_class': forms.Select(attrs={'class': 'form-control'}),
            'total_fees': forms.NumberInput(attrs={'class': 'form-control'}),
            'paid_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# end of new form 

# class FeesForm(forms.ModelForm):
#     class Meta:
#         model = Fees
#         fields = ['roll_ID', 'studend', 'classes', 'fees_amount', 'paid_fees', 'blance_fees', 'fees_status']
#         labels = {
#             'roll_ID': 'Roll ID',
#             'studend': 'Student',
#             'classes': 'Class',
#             'fees_amount': 'Fees Amount',
#             'paid_fees': 'Paid Fees',
#             'blance_fees': 'Balance Fees',
#             'fees_status': 'Fees Status',
#         }

#     def __init__(self, *args, **kwargs):
#         super(FeesForm, self).__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs.update({
#                 'class': 'form-control mb-2',
#                 'placeholder': field.label
#             })



from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

         
# new sign up forms
# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'photo']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Save photo in profile
            if self.cleaned_data.get('photo'):
                user.profile.photo = self.cleaned_data['photo']
                user.profile.save()
        return user

    
      
      
  