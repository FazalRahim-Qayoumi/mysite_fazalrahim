
from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path
from . import views
# from django.conf import settings
from django.conf.urls.static import static


# do here
urlpatterns = [
    path('teachers/', views.Teacher_page, name='teacher_page'),
    path('teachers/csv/', views.download_csv, name='download_csv'),
    path('teachers/pdf/', views.download_pdf, name='download_pdf'),

     path('parents/', views.Parent_page, name='parent_page'),
    path('parents/csv/', views.download_parents_csv, name='download_parents_csv'),
    path('parents/pdf/', views.download_parents_pdf, name='download_parents_pdf'),

    path('subjects/', views.subject_page, name='Subject_page'),
    path('subjects/download/csv/', views.download_subject_csv, name='download_subject_csv'),
    path('subjects/download/pdf/', views.download_subject_pdf, name='download_subject_pdf'),

    path('Student_page/', views.student_page, name='Student_page'),
    path('students/download/csv/', views.download_student_csv, name='download_student_csv'),
    path('students/download/pdf/', views.download_student_pdf, name='download_student_pdf'),

    path('Marks_page/', views.marks_page, name='Marks_page'),
    path('marks/download/csv/', views.download_marks_csv, name='download_marks_csv'),
    path('marks/download/pdf/', views.download_marks_pdf, name='download_marks_pdf'),

        path('Attendance_page/', views.attendance_page, name='Attendance_page'),
    path('attendance/download/csv/', views.download_attendance_csv, name='download_attendance_csv'),
    path('attendance/download/pdf/', views.download_attendance_pdf, name='download_attendance_pdf'),

    path('Staff_page/', views.staff_page, name='Staff_page'),
    path('staff/download/csv/', views.download_staff_csv, name='download_staff_csv'),
    path('staff/download/pdf/', views.download_staff_pdf, name='download_staff_pdf'),

    path('fees/', views.fees_list, name='fees_list'),
    path('fees/pdf/', views.fees_report_pdf, name='fees_report_pdf'),
    # path('Fees_page/', views.fees_page, name='Fees_page'),
    # path('fees/download/csv/', views.download_fees_csv, name='download_fees_csv'),
    # path('fees/download/pdf/', views.download_fees_pdf, name='download_fees_pdf'),

    path('Class_page/', views.class_page, name='Class_page'),
    path('class/download/csv/', views.download_class_csv, name='download_class_csv'),
    path('class/download/pdf/', views.download_class_pdf, name='download_class_pdf'),

    path('dashboard/',views.dashboard , name='dashboard'),
    # path('dashboard/',views.dashboard , name='dashboard'),
    path('teacher_page/<int:id>',views.Teacher_page , name='teacher_page'),
   
    path('dashboard1/', views.dashboard_total, name='dashboard'),
    path('logout/', views.log_out, name='logout'),
    path("login/",views.login_page,name="login"),
    path('signup/', views.signup_view, name='signup'),
    path('', views.signup, name='signup1'),
    path('profile/', views.profile, name='profile'),

    #  path('pdf/', views.generate_pdf, name='generate_pdf'),

]
if settings.DEBUG:urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
if settings.DEBUG:urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)