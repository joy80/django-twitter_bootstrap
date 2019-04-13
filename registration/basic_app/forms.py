from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo

class UserForm(forms.ModelForm):
    username = forms.CharField(label='Name',max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password','confirm_password')


    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


# class UserProfileInfoForm(forms.ModelForm):
#     class Meta():
#         model = UserProfileInfo
#         fields = ('portfolio_site','profile_pic')
