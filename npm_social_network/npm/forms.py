from django import forms
from django.forms import ModelForm
from .models import User

class RegisterForm(ModelForm):
    class Meta:
        model = User 
        fields = "__all__"

        # labels = {
        #     'first_name':'',
        #     'last_name':'',
        #     'local_gov':'',
        #     'phone_number': '',
        #     'state':'',
        #     'email':'',
        #     'password':'',
        # }

        # widgets = {
        #     'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}),
        #     'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}),
        #     'state':forms.TextInput(attrs={'class':'form-control','placeholder':'state'}),
        #     'local_gov':forms.TextInput(attrs={'class':'form-control','placeholder':'local goverment'}),
        #     'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'mobile number'}),
        #     'password':forms.TextInput(attrs={'class':'form-control','placeholder':'password'}),
        #     'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email address'}),
   
        # }

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.state = self.cleaned_data['state']
        user.local_gov = self.cleaned_data['local_gov']
        user.phone_number = self.cleaned_data['phone_number']

        if commit:
            user.save()
        
        return user
    

# class LoginForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('email', 'password')

#         labels = {
#             'email':'',
#             'passwd':'',
#         }

#         widgets = {
#             'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
#             'password':forms.TextInput(attrs={'class':'from-control','placeholder':'password'})
#         }

