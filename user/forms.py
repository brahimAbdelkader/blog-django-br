from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserCreationForm(forms.ModelForm):
    
    username   = forms.CharField(label='اسم المستخدم',max_length=30 ,help_text='اسم المستخدم يجب الا يحتوي على مسافات او رموز')
    email      = forms.EmailField(label='البريد الالكتروني')
    first_name = forms.CharField(label='اسم الاول', max_length=100)
    last_name  = forms.CharField(label='اسم الاخير', max_length=100)
    password1  = forms.CharField(
        label='كلمة المرور',widget=forms.PasswordInput() ,min_length=8)
    password2  = forms.CharField(
        label=' تاكيد كلمة المرور ', widget=forms.PasswordInput())
    
    class Meta:
        model=User
        fields =('username','email','first_name',
                 'last_name', 'password1', 'password2')

    # def clear_password2(self):
    
    #     cd = self.cleaned_data
    #     if cd['password1'] != cd['password2']:      
    #         raise forms.ValidationError('كلمة المرور غير متطابقة')        
    #     return cd['password2']    
         
    
         
         
         
    def clean_username(self):
        cd= self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError ('هذا المستخدم مسجل مسبقا')
            
        return cd['username']
    
    
    def clean_email(self):
        existing = User.objects.filter(
            email__iexact=self.cleaned_data['email'])
        if existing.exists():
            raise forms.ValidationError('هذا الايميل تم استعماله مسبقا')
        return self.cleaned_data['email']


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data.get("password2", "")
        if password1 and password2:  # If both passwords has value
                if password1 != password2:
                    raise forms.ValidationError("كلمة المرور غير متطابقة")
                # else:
                #     raise forms.ValidationError("لا يمكن ترك هذا الحقل فارغا")
                return password2


class LoginForm(forms.ModelForm):
    
    username = forms.CharField(label='اسم المستخدم')
    password = forms.CharField(label= 'كلمة المرور',widget=forms.PasswordInput())
    class Meta:
        model  =User
        fields = ('username','password')
        
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='البريد الالكتروني')
    first_name = forms.CharField(label='اسم الاول', max_length=100)
    last_name = forms.CharField(label='اسم الاخير', max_length=100)
    class Meta:
        model=User
        fields=('first_name','last_name','email',)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('image',)
