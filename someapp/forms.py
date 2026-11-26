from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserWithPhone, Request

class UserWithPhoneCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserWithPhone
        fields = ("username", "phone")

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['course', 'comment']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance