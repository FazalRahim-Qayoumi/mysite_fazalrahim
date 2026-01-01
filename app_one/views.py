
from multiprocessing import context
from xhtml2pdf import pisa
from os import name
import re
from sys import stderr
from tkinter import NO
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from requests import get, post
from . forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from .models import  Class,Parent,Marks,Attendance,Student,Subject,Teacher ,Staff,Fees
from .models import Parent
from .forms import ParentForm


# Create your views here.
# def dashboard(request):
#     techers=Teacher.objects.all()
#     cont={
#         "teacher":techers,
#     }
#     return render(request,'dashboard.html',cont)




from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import Teacher
from .forms import TeacherForm
import csv
from reportlab.pdfgen import canvas

def Teacher_page(request):
    query = request.GET.get('q', '')
    if query:
        teachers = Teacher.objects.filter(
            Q(name__icontains=query) |
            Q(subject__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query)
        )
    else:
        teachers = Teacher.objects.all()

    form = TeacherForm()

    # Add new teacher
    if request.method == 'POST' and 'add_teacher' in request.POST:
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_page')

    # Edit teacher
    if request.method == 'POST' and 'edit_teacher' in request.POST:
        teacher_id = request.POST.get('teacher_id')
        teacher = get_object_or_404(Teacher, id=teacher_id)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_page')

    # Delete teacher
    if request.method == 'POST' and 'delete_teacher' in request.POST:
        teacher_id = request.POST.get('teacher_id')
        teacher = get_object_or_404(Teacher, id=teacher_id)
        teacher.delete()
        return redirect('teacher_page')

    return render(request, 'teacher_page.html', {
        'teachers': teachers,
        'form': form,
        'query': query
    })


# CSV download
def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="teachers.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Subject', 'Phone', 'Email'])
    for t in Teacher.objects.all():
        writer.writerow([t.name, t.subject, t.phone, t.email])
    return response


# PDF download
def download_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="teachers.pdf"'
    p = canvas.Canvas(response)
    y = 800
    p.drawString(100, y, "Teachers List")
    y -= 30
    for t in Teacher.objects.all():
        line = f"{t.name} | {t.subject} | {t.phone} | {t.email}"
        p.drawString(100, y, line)
        y -= 20
    p.showPage()
    p.save()
    return response

# finish Teacher section 

# Parent section start 
def Parent_page(request):
    query = request.GET.get('q', '')
    if query:
        parents = Parent.objects.filter(
            Q(name__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query) |
            Q(address__icontains=query)
        )
    else:
        parents = Parent.objects.all()

    form = ParentForm()

    # Add parent
    if request.method == 'POST' and 'add_parent' in request.POST:
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parent_page')

    # Edit parent
    if request.method == 'POST' and 'edit_parent' in request.POST:
        parent_id = request.POST.get('parent_id')
        parent = get_object_or_404(Parent, id=parent_id)
        form = ParentForm(request.POST, instance=parent)
        if form.is_valid():
            form.save()
            return redirect('parent_page')

    # Delete parent
    if request.method == 'POST' and 'delete_parent' in request.POST:
        parent_id = request.POST.get('parent_id')
        parent = get_object_or_404(Parent, id=parent_id)
        parent.delete()
        return redirect('parent_page')

    return render(request, 'parent_page.html', {'parents': parents,'form': form, 'query': query})


# CSV download
def download_parents_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="parents.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Phone', 'Email', 'Address'])
    for p in Parent.objects.all():
        writer.writerow([p.name, p.phone, p.email, p.address])
    return response


# PDF download
def download_parents_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="parents.pdf"'
    p = canvas.Canvas(response)
    y = 800
    p.drawString(100, y, "Parents List")
    y -= 30
    for pa in Parent.objects.all():
        line = f"{pa.name} | {pa.phone} | {pa.email} | {pa.address}"
        p.drawString(100, y, line)
        y -= 20
    p.showPage()
    p.save()
    return response

# finish Parent section
 
from .models import Subject, Teacher
from .forms import SubjectForm


def subject_page(request):
    query = request.GET.get('q', '')
    if query:
        subjects = Subject.objects.filter(
            Q(name__icontains=query) |
            Q(code__icontains=query) |
            Q(teacher__name__icontains=query)
        )
    else:
        subjects = Subject.objects.all()

    form = SubjectForm()

    # Add
    if request.method == 'POST' and 'add_subject' in request.POST:
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Subject_page')

    # Edit
    if request.method == 'POST' and 'edit_subject' in request.POST:
        subject_id = request.POST.get('subject_id')
        subject = get_object_or_404(Subject, id=subject_id)
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('Subject_page')

    # Delete
    if request.method == 'POST' and 'delete_subject' in request.POST:
        subject_id = request.POST.get('subject_id')
        subject = get_object_or_404(Subject, id=subject_id)
        subject.delete()
        return redirect('Subject_page')

    return render(request, 'subject_page.html', {'subjects': subjects,'form': form,'query': query})


# Download CSV
def download_subject_csv(request):
    subjects = Subject.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="subjects.csv"'
    writer = csv.writer(response)
    writer.writerow(['Subject Name', 'Code', 'Teacher'])
    for s in subjects:
        teacher_name = s.teacher.name if s.teacher else 'No Teacher'
        writer.writerow([s.name, s.code, teacher_name])
    return response


# Download PDF
def download_subject_pdf(request):
    subjects = Subject.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="subjects.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 14)
    p.drawString(230, 800, "Subject List")
    y = 760
    p.setFont("Helvetica", 12)
    for s in subjects:
        teacher_name = s.teacher.name if s.teacher else 'No Teacher'
        p.drawString(50, y, f"{s.name} | {s.code} | {teacher_name}")
        y -= 20
        if y < 50:
            p.showPage()
            y = 800
    p.save()
    return response

# Subject section finish


# Student section start 
from .models import Student
from .forms import StudentForm

def student_page(request):
    query = request.GET.get('q', '')
    if query:
        students = Student.objects.filter(
            Q(name__icontains=query) |
            Q(roll_no__icontains=query) |
            Q(student_class__name__icontains=query) |
            Q(parent__name__icontains=query)
        )
    else:
        students = Student.objects.all()

    form = StudentForm()

    # Add student
    if request.method == 'POST' and 'add_student' in request.POST:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Student_page')

    # Edit student
    if request.method == 'POST' and 'edit_student' in request.POST:
        student_id = request.POST.get('student_id')
        student = get_object_or_404(Student, id=student_id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('Student_page')

    # Delete student
    if request.method == 'POST' and 'delete_student' in request.POST:
        student_id = request.POST.get('student_id')
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        return redirect('Student_page')

    return render(request, 'student_page.html', {
        'students': students,
        'form': form,
        'query': query
    })

# CSV download
def download_student_csv(request):
    students = Student.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Roll No', 'DOB', 'Gender', 'Class', 'Address', 'Parent'])
    for s in students:
        writer.writerow([
            s.name, s.roll_no, s.date_of_birth, s.get_gender_display(),
            s.student_class.name, s.address, s.parent.name
        ])
    return response

# PDF download
def download_student_pdf(request):
    students = Student.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="students.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 14)
    p.drawString(200, 800, "Student List")
    y = 760
    p.setFont("Helvetica", 12)
    for s in students:
        line = f"{s.name} | {s.roll_no} | {s.date_of_birth} | {s.get_gender_display()} | {s.student_class.name} | {s.parent.name}"
        p.drawString(50, y, line)
        y -= 20
        if y < 50:
            p.showPage()
            y = 800
    p.save()
    return response
#  student section  is finish 

# Marks sectiion is start 

from .models import Marks
from .forms import MarksForm

def marks_page(request):
    query = request.GET.get('q', '')
    if query:
        marks_list = Marks.objects.filter(
            Q(student__name__icontains=query) |
            Q(subject__name__icontains=query) |
            Q(exam_type__icontains=query)
        )
    else:
        marks_list = Marks.objects.all()

    form = MarksForm()

    # Add marks
    if request.method == 'POST' and 'add_marks' in request.POST:
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Marks_page')
        

    # Edit marks
    if request.method == 'POST' and 'edit_marks' in request.POST:
        marks_id = request.POST.get('marks_id')
        marks = get_object_or_404(Marks, id=marks_id)
        form = MarksForm(request.POST, instance=marks)
        if form.is_valid():
            form.save()
            return redirect('Marks_page')

    # Delete marks
    if request.method == 'POST' and 'delete_marks' in request.POST:
        marks_id = request.POST.get('marks_id')
        marks = get_object_or_404(Marks, id=marks_id)
        marks.delete()
        return redirect('Marks_page')

    return render(request, 'marks_page.html', {
        'marks_list': marks_list,
        'form': form,
        'query': query
    })

# CSV download
def download_marks_csv(request):
    marks_list = Marks.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="marks.csv"'
    writer = csv.writer(response)
    writer.writerow(['Student', 'Subject', 'Marks Obtained', 'Exam Type'])
    for m in marks_list:
        writer.writerow([m.student.name, m.subject.name, m.marks_obtained, m.exam_type])
    return response

# PDF download
def download_marks_pdf(request):
    marks_list = Marks.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="marks.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 14)
    p.drawString(200, 800, "Marks List")
    y = 760
    p.setFont("Helvetica", 12)
    for m in marks_list:
        line = f"{m.student.name} | {m.subject.name} | {m.marks_obtained} | {m.exam_type}"
        p.drawString(50, y, line)
        y -= 20
        if y < 50:
            p.showPage()
            y = 800
    p.save()
    return response
# marks section is finish 
# Attendance section is start 
from .models import Attendance
from .forms import AttendanceForm

def attendance_page(request):
    query = request.GET.get('q', '')
    if query:
        attendance_list = Attendance.objects.filter(
            Q(student__name__icontains=query) |
            Q(date__icontains=query)
        )
    else:
        attendance_list = Attendance.objects.all()

    form = AttendanceForm()

    # Add
    if request.method == 'POST' and 'add_attendance' in request.POST:
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Attendance_page')

    # Edit
    if request.method == 'POST' and 'edit_attendance' in request.POST:
        attendance_id = request.POST.get('attendance_id')
        record = get_object_or_404(Attendance, id=attendance_id)
        form = AttendanceForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('Attendance_page')

    # Delete
    if request.method == 'POST' and 'delete_attendance' in request.POST:
        attendance_id = request.POST.get('attendance_id')
        record = get_object_or_404(Attendance, id=attendance_id)
        record.delete()
        return redirect('Attendance_page')

    return render(request, 'attendance_page.html', {
        'attendance_list': attendance_list,
        'form': form,
        'query': query
    })

# CSV download
def download_attendance_csv(request):
    attendance_list = Attendance.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendance.csv"'
    writer = csv.writer(response)
    writer.writerow(['Student', 'Date', 'Status'])
    for a in attendance_list:
        writer.writerow([a.student.name, a.date, a.get_status_display()])
    return response

# PDF download
def download_attendance_pdf(request):
    attendance_list = Attendance.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="attendance.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 14)
    p.drawString(200, 800, "Attendance List")
    y = 760
    p.setFont("Helvetica", 12)
    for a in attendance_list:
        line = f"{a.student.name} | {a.date} | {a.get_status_display()}"
        p.drawString(50, y, line)
        y -= 20
        if y < 50:
            p.showPage()
            y = 800
    p.save()
    return response

# marks section is finish 

# Staff section is start 
from .models import Staff
from .forms import StaffForm
def staff_page(request):
    query = request.GET.get('q', '')
    if query:
        staff_list = Staff.objects.filter(
            Q(prancipal__icontains=query) |
            Q(vice_prancipal__icontains=query) |
            Q(School_secretary__icontains=query) |
            Q(Accountant__icontains=query) |
            Q(librarian__icontains=query) |
            Q(IT_technation__icontains=query) |
            Q(guard__icontains=query) |
            Q(cleaner__icontains=query) |
            Q(Subject_teacher__name__icontains=query)
        )
    else:
        staff_list = Staff.objects.all()

    form = StaffForm()

    # Add
    if request.method == 'POST' and 'add_staff' in request.POST:
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Staff_page')

    # Edit
    if request.method == 'POST' and 'edit_staff' in request.POST:
        staff_id = request.POST.get('staff_id')
        staff = get_object_or_404(Staff, id=staff_id)
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('Staff_page')

    # Delete
    if request.method == 'POST' and 'delete_staff' in request.POST:
        staff_id = request.POST.get('staff_id')
        staff = get_object_or_404(Staff, id=staff_id)
        staff.delete()
        return redirect('Staff_page')

    return render(request, 'staff_page.html', {
        'staff_list': staff_list,
        'form': form,
        'query': query
    })


# CSV download
def download_staff_csv(request):
    staff_list = Staff.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="staff.csv"'
    writer = csv.writer(response)
    writer.writerow(['Principal', 'Vice Principal', 'School Secretary', 'Accountant', 'Subject Teacher', 'Librarian', 'IT Technician', 'Guard', 'Cleaner'])
    for s in staff_list:
        writer.writerow([
            s.prancipal, s.vice_prancipal, s.School_secretary, s.Accountant,
            s.Subject_teacher.name if s.Subject_teacher else 'No Teacher',
            s.librarian, s.IT_technation, s.guard, s.cleaner
        ])
    return response


# PDF download
def download_staff_pdf(request):
    staff_list = Staff.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="staff.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 14)
    p.drawString(180, 800, "Staff List")
    y = 760
    p.setFont("Helvetica", 12)
    for s in staff_list:
        line = f"{s.prancipal} | {s.vice_prancipal} | {s.School_secretary} | {s.Accountant} | {s.Subject_teacher.name if s.Subject_teacher else 'No Teacher'} | {s.librarian} | {s.IT_technation} | {s.guard} | {s.cleaner}"
        p.drawString(50, y, line)
        y -= 20
        if y < 50:
            p.showPage()
            y = 800
    p.save()
    return response

# Staff section is finish 


# new fee 

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Fees
from .forms import FeesForm
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def fees_list(request):
    fees = Fees.objects.all().order_by('-payment_date')
    form = FeesForm()

    # CREATE
    if request.method == 'POST' and 'add_fees' in request.POST:
        form = FeesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fees_list')

    # UPDATE
    if request.method == 'POST' and 'update_fees' in request.POST:
        fee = get_object_or_404(Fees, pk=request.POST.get('fee_id'))
        form = FeesForm(request.POST, instance=fee)
        if form.is_valid():
            form.save()
            return redirect('fees_list')

    # DELETE
    if request.method == 'POST' and 'delete_fees' in request.POST:
        fee = get_object_or_404(Fees, pk=request.POST.get('fee_id'))
        fee.delete()
        return redirect('fees_list')

    return render(request, 'fees_list.html', {'fees': fees, 'form': form})


def fees_report_pdf(request):
    """Generate PDF report of all fees"""
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Fees_Report.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter
    y = height - 50

    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, y, "School Fees Report")
    y -= 40

    p.setFont("Helvetica-Bold", 10)
    p.drawString(40, y, "Student")
    p.drawString(150, y, "Class")
    p.drawString(250, y, "Total")
    p.drawString(310, y, "Paid")
    p.drawString(370, y, "Balance")
    p.drawString(450, y, "Status")
    y -= 20

    p.setFont("Helvetica", 10)
    fees = Fees.objects.all()
    for fee in fees:
        p.drawString(40, y, str(fee.student))
        p.drawString(150, y, str(fee.student_class))
        p.drawString(250, y, str(fee.total_fees))
        p.drawString(310, y, str(fee.paid_amount))
        p.drawString(370, y, str(fee.balance_amount))
        p.drawString(450, y, fee.status.capitalize())
        y -= 18
        if y < 50:
            p.showPage()
            y = height - 50
            p.setFont("Helvetica", 10)

    p.showPage()
    p.save()
    return response


# end of new fee 

# total fees section 

from django.db.models import Sum
from django.shortcuts import render
from .models import Fees

def dashboard_total(request):
    
    # Calculate totals
    totals = Fees.objects.aggregate(
        total_sum=Sum('total_fees'),
        paid_sum=Sum('paid_amount'),
        balance_sum=Sum('balance_amount')
    )

    # Default to 0 if None
    totals = {k: v or 0 for k, v in totals.items()}
    techers=Teacher.objects.all()
    cont={
        "teacher":techers,
        'totals': totals
    }

    return render(request, 'dashboard.html', cont)



# class section is start 
from .models import Class
from .forms import ClassForm

 
def class_page(request):
    query = request.GET.get('q', '')
    if query:
        class_list = Class.objects.filter(
            Q(name__icontains=query) |
            Q(section__icontains=query) |
            Q(class_teacher__icontains=query)
        )
    else:
        class_list = Class.objects.all()

    form = ClassForm()

    # Add
    if request.method == 'POST' and 'add_class' in request.POST:
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Class_page')

    # Edit
    if request.method == 'POST' and 'edit_class' in request.POST:
        class_id = request.POST.get('class_id')
        record = get_object_or_404(Class, id=class_id)
        form = ClassForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('Class_page')

    # Delete
    if request.method == 'POST' and 'delete_class' in request.POST:
        class_id = request.POST.get('class_id')
        record = get_object_or_404(Class, id=class_id)
        record.delete()
        return redirect('Class_page')

    return render(request, 'class_page.html', {
        'class_list': class_list,
        'form': form,
        'query': query
    })


# CSV download
def download_class_csv(request):
    class_list = Class.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="class.csv"'
    writer = csv.writer(response)
    writer.writerow(['Class Name', 'Section', 'Class Teacher'])
    for c in class_list:
        writer.writerow([c.name, c.section, c.class_teacher])
    return response


# PDF download
def download_class_pdf(request):
    class_list = Class.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="class.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 14)
    p.drawString(220, 800, "Class List")
    y = 760
    p.setFont("Helvetica", 12)
    for c in class_list:
        line = f"{c.name} | {c.section} | {c.class_teacher}"
        p.drawString(50, y, line)
        y -= 20
        if y < 50:
            p.showPage()
            y = 800
    p.save()
    return response


# login page
# @login_required(login_url='login')
def login_page(request):
    if request.method=="POST":
        username=request.POST.get("name")
        password=request.POST.get("password")
        valid_dat=authenticate(request, username=username,password=password)
        if valid_dat is not None:
            login(request,valid_dat)
            return redirect('dashboard')
        else:
            return HttpResponse("increcct password enter ")
    return render(request,'login.html')

 






# sign up function
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}!')
            return redirect('login')  # 👈 change 'login' to your login page name
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})
# new signup page 


# views.py
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)  # important for images
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('profile')
    else:
        form = SignupForm()
    return render(request, 'signup1.html', {'form': form})


@login_required
def profile(request):
    pr=profile.obects.all()
    return render(request, 'profile.html', {'user': request.user})
# end of new signup

# logout page 
    
def log_out(request):
    logout(request)
    return redirect('login')




# access level of roles 
# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Sum

@login_required
def dashboard(request):
    user = request.user

    context = {
        'user': user,
        'role': user.role,
    }

    # You already calculate totals, so include them too
    # Example if you use Fees model:
    from .models import Fees

    totals = {
    'total_sum': Fees.objects.aggregate(total=Sum('total_fees'))['total'],
    'paid_sum': Fees.objects.aggregate(paid=Sum('paid_amount'))['paid'],
    'balance_sum': Fees.objects.aggregate(balance=Sum('balance_amount'))['balance'],
    }
    context['totals'] = totals

    return render(request, 'new_da.html', context)

