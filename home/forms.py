# # from django import forms

# # class Register(forms.Form):
# #    fname = forms.CharField(max_length=122)
# #    lname = forms.CharField(max_length=122)
# #    email = forms.CharField(max_length=122)
# #    number = forms.CharField(max_length=12)
# #    password=forms.CharField(widget=forms.PasswordInput)
# #    rpassword=forms.CharField(label='Password(again)',widget=forms.PasswordInput)
# #    def clean(self):
# #       cleaned_data=super().clean()
# #       valpwd=cleaned_data['password']
# #       valrpwd=cleaned_data['rpassword']
# #       if valpwd!=valrpwd:
# #          raise forms.ValidationError('Password not match')

# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# class UserRegisterForm(UserCreationForm):
#     email=forms.EmailField(max_length=100,help_text='Required,Inform a valid email address')
#     class Meta:
#         model = User
#         fields=['username','email','password1','password2']