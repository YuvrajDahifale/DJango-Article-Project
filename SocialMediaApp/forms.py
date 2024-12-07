from django import forms
from .models import Article
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Enter First Name",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Your First Name',
            'class': 'form-control mb-3 mt-2'
        })
    )
    
    last_name = forms.CharField(
        label="Enter Last Name",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Your Last Name',
            'class': 'form-control mb-3 mt-2'
        })
    )
    
    email = forms.EmailField(
        label="Enter Email Name",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter Your Email Name',
            'class': 'form-control mb-3 mt-2'
        })
    )
    
    username = forms.CharField(
        label="Enter Username Name",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Username Name',
            'class': 'form-control mb-3 mt-2'
        })
    )
    
    password = forms.CharField(
        label="Enter Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter Password',
            'class': 'form-control mb-3 mt-2'
        })
    )
    
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control mb-3 mt-2'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
# ===============================================================================================

class UserLoginForm(forms.Form):
    username = forms.CharField(
        label="Enter UserName",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter UserName',
                'class': 'form-control mb-3 mt-2'
            }
        )

    ) 

    password = forms.CharField(
        label="Enter Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter Password',
                'class': 'form-control mt-3',
                'row':10,
                'cols':50
            }
        )

    )

# ===============================================================================================

class ArticleCreatedForm(forms.Form):
    title = forms.CharField(
        label="Enter Title",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Title',
                'class': 'form-control mb-3 mt-2 '
            }
        )

    ) 

    body = forms.CharField(
        label="Enter Content",
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter Content ',
                'class': 'form-control mt-2 ',
                'row':10,
                'cols':50
            }
        )

    )

