from django import forms
from .models import Account,user

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter password',
        'class':'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'confirm password',
        'class':'form-control',
    }))
    
    class Meta:
        model = Account
        fields = ['first_name','last_name','email','username'] 
        
    def clean(self):
        cleaned_data = super(RegistrationForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError(
                'Password does not match'
            )    
        
    def __init__(self,*args, **kwargs):
        super(RegistrationForm,self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder']= 'First Name '
        self.fields['last_name'].widget.attrs['placeholder']= 'last Name '
        self.fields['email'].widget.attrs['placeholder']= 'Email'
        self.fields['username'].widget.attrs['placeholder']= 'username'
        for field in self.fields:
            self.fields[field].widget.attrs['class']= 'form-control'    
            
class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields= ['first_name','last_name']
        
    def __init__(self,*args, **kwargs):
        super(UserForm,self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']= 'form-control'
            
        
class userForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['first_name','last_name','email']
        
    def __init__(self,*args, **kwargs):
        super(UserForm,self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']= 'form-control'     
                           