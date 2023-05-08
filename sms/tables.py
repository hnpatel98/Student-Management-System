from django_tables2 import tables, Column, TemplateColumn
from sms.models import StudentDepartmentMapper, Subject, TeacherSubjectMapper


class StudentDepartmentTable(tables.Table):
    view = TemplateColumn(template_name='sms/table/action_columns/student_actions.html',
                          orderable=False)

    class Meta:
        model = StudentDepartmentMapper
        fields = ("id", "student.user_define_id", "department", "view")

    def before_render(self, request):
        self.columns.hide('id')


class SubjectTable(tables.Table):
    taken_by = Column(accessor='pk', verbose_name="Taken by")

    class Meta:
        model = Subject
        fields = ("id", "name", "code", "credit", "taken_by")

    def before_render(self, request):
        self.columns.hide('id')

    @staticmethod
    def render_taken_by(record: Subject):
        print(TeacherSubjectMapper.objects.filter(subject=record))
        teacher_list = TeacherSubjectMapper.objects.filter(subject=record).values_list('teacher__user_define_id',
                                                                                       flat=True)
        return ','.join(teacher_list)
