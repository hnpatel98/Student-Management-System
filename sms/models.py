from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_define_id = models.CharField(unique=True, max_length=20, verbose_name="User ID")

    STUDENT = 'student'
    TEACHER = 'teacher'

    USER_TYPE = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE, default=STUDENT)

    GENDER_TYPE = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_TYPE, default=GENDER_TYPE[0][0])
    dob = models.DateField(blank=True, null=True)
    address = models.TextField(verbose_name="Residence Address")
    contact_no = models.IntegerField()

    def __str__(self):
        return self.user.username


class Department(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=10)
    description = models.TextField()
    created_by = models.ForeignKey(User, related_name='%(class)s_created_by', on_delete=models.SET_NULL,
                                   null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=10)
    credit = models.FloatField(default=0)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='%(class)s_created_by', on_delete=models.SET_NULL, null=True,
                                   blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TeacherSubjectMapper(models.Model):
    teacher = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    subject = models.ManyToManyField(Subject)
    created_by = models.ForeignKey(User, related_name='%(class)s_created_by', on_delete=models.SET_NULL, null=True,
                                   blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.teacher.user.username


class StudentDepartmentMapper(models.Model):
    student = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='%(class)s_created_by', on_delete=models.SET_NULL, null=True,
                                   blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.user.username
