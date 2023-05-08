from django.contrib import admin

from sms.models import Department, Subject, StudentDepartmentMapper, TeacherSubjectMapper, UserProfile

# Register your models here.

admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(UserProfile)
admin.site.register(StudentDepartmentMapper)
admin.site.register(TeacherSubjectMapper)
