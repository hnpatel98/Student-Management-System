from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import transaction
from django.urls import reverse
from django.utils import timezone
from django.views.generic import TemplateView, CreateView, DetailView
from django_tables2 import SingleTableView

from sms.forms import UserProfileForm
from sms.models import StudentDepartmentMapper, UserProfile, Department, Subject
from sms.tables import StudentDepartmentTable, SubjectTable


class Login(views.LoginView):
    template_name = 'sms/login.html'
    first_time_login = False

    def form_valid(self, form):
        user = form.get_user()
        self.first_time_login = user.last_login
        return super(Login, self).form_valid(form)

    def get_success_url(self):
        try:
            date_difference = timezone.now() - self.first_time_login
        except:
            date_difference = timezone.now() - timezone.now()
        if not self.first_time_login or date_difference.days >= 30:
            return reverse('change-password')
        else:
            if self.request.user.userprofile.user_type == self.request.user.userprofile.STUDENT:
                return reverse('courseList')
            else:
                return reverse('studentList')


class PasswordChange(views.PasswordChangeView):
    template_name = 'sms/password_change.html'

    def get_success_url(self):
        if self.request.user.userprofile.user_type == self.request.user.userprofile.STUDENT:
            return reverse('courseList')
        else:
            return reverse('studentList')


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'sms/home.html'


class StudentList(LoginRequiredMixin, SingleTableView):
    model = StudentDepartmentMapper
    table_class = StudentDepartmentTable
    template_name = 'sms/student_list.html'

    def get_queryset(self):
        query = super(StudentList, self).get_queryset()
        # if not self.request.user.is_superuser:
        #     query = query.filter(
        #         siteauthsetting__in=model_site.SiteAuthSetting.objects.filter(user=self.request.user))
        return query


class StudentCreate(LoginRequiredMixin, CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'sms/create_student.html'

    @transaction.atomic()
    def form_valid(self, form):
        if form.is_valid():
            user: User = User.objects.create_user(username=form.cleaned_data['user_define_id'], password='Chembond@123',
                                                  first_name=form.cleaned_data['first_name'],
                                                  last_name=form.cleaned_data['last_name'])
            user.set_password(user.last_name)
            user.save()
            form.instance.user = user
            form.instance.user_type = UserProfile.STUDENT
            self.object = form.save()
            StudentDepartmentMapper.objects.create(student=self.object, department=form.cleaned_data['department'],
                                                   created_by=self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('studentList')


class DepartmentCoursesDetail(LoginRequiredMixin, DetailView):
    model = Department
    template_name = 'sms/department_course_detail.html'


class CourseList(LoginRequiredMixin, SingleTableView):
    model = Subject
    table_class = SubjectTable
    template_name = 'sms/course_list.html'

    def get_queryset(self):
        query = super(CourseList, self).get_queryset()
        if not self.request.user.is_superuser:
            query = query.filter(department=self.request.user.userprofile.studentdepartmentmapper.department)
        return query
