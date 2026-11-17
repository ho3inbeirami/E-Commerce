from django import forms
from account_module.models import User
from django.core.exceptions import ValidationError
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'address','about']

        widgets = {
            'first_name': forms.TextInput(
                attrs= {
                    'class':'form-control'
                }
            ),
            'last_name': forms.TextInput(
                            attrs= {
                                'class':'form-control'
                            }
            ),
            'avatar': forms.FileInput(
                            attrs= {
                                'class':'form-control'
                            }
            
            ),
            'address': forms.TextInput(
                            attrs= {
                                'class':'form-control',
                                'id':'message',
                                'rows':5,
                            }
                        ),
            'about': forms.TextInput(
                            attrs= {
                                'class':'form-control'
                            }
            ),
        }
        
class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'',
                'placeholder':'Current Password'
            }
        )
    )
    new_password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'',
                'placeholder':'New Password'
            }
        )
    )
    confirm_new_password =forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'',
                'placeholder':'New Confirm Password'
            }
        )
    )


    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        
        if password == confirm_password:
            return confirm_password
        
        raise ValidationError('password and confirm password most be unique')
