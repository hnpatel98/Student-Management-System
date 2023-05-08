from django.urls import path
from django.contrib.auth import views as auth_views

from sms import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('change-password/', views.PasswordChange.as_view(), name='change-password'),
    path('student_list/', views.StudentList.as_view(), name='studentList'),
    path('student_create/', views.StudentCreate.as_view(), name='studentCreate'),
    path('<int:pk>/course_details/', views.DepartmentCoursesDetail.as_view(), name='departmentCoursesDetail'),
    path('course_list/', views.CourseList.as_view(), name='courseList'),
]
