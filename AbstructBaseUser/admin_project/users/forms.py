from django import forms
from django.contrib.auth import get_user_model


class SignupForm(forms.ModelForm):

    """user signup form"""
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
    	cleaned_data = super().clean()
    	password     = cleaned_data.get('password')
    	password_confirm = cleaned_data.get('password_confirm')
    	if password and password_confirm:
    		if password != password_confirm:
    			raise forms.ValidationError("two password should match!")


    class Meta:
        model = get_user_model()
        fields = ('email', 'name','mobile_number', 'password','password_confirm')

    
    # def clean(self):
    # 	cleaned_data = super(SignupForm, self).clean()
    	
    # 	password = cleaned_data.get('password')
    # 	password_confirm = cleaned_data.get('password_confirm ')

    # 	if password and password_confirm:
    # 		if password != password_confirm:
    # 			raise forms.ValidationError("The two password fields must match.")
    # 	return cleaned_data


class LoginForm(forms.Form):
    """user login form"""
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
