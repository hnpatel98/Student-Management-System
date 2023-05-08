from django.contrib.auth.models import User
from django.forms import forms, ModelForm, CharField, EmailField, ModelChoiceField
from bootstrap_datepicker_plus.widgets import DatePickerInput

from sms.models import UserProfile, Department


class UserProfileForm(ModelForm):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    email = EmailField(max_length=254)
    department = ModelChoiceField(queryset=Department.objects.all())

    class Meta:
        model = UserProfile
        fields = ['user_define_id', 'gender', 'address', 'contact_no', 'first_name', 'last_name', 'email', 'department']

    def clean(self):
        super(UserProfileForm, self).clean()
        if User.objects.filter(username=self.cleaned_data['user_define_id']).exists():
            self._errors['user_define_id'] = self.error_class(['Already Registered.'])
        return self.cleaned_data
