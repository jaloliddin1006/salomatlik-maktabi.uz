from django import forms
from django.forms.widgets import TextInput, PasswordInput, EmailInput
from .models import User

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder':'username:'}), required=True)
    email = forms.CharField(widget=TextInput(attrs={'placeholder':'email manzilingizni kiriting:'}), required=True)
    first_name = forms.CharField(widget=TextInput(attrs={'placeholder':'ismingizni kiriting:'}), required=True)
    last_name = forms.CharField(widget=TextInput(attrs={'placeholder':'familiyangizni kiriting:'}), required=True)
    phone = forms.CharField(widget=TextInput(attrs={'placeholder':'telefon nomeringizni kiriting:'}), required=True)
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'password:'}), required=True)
    confirm_password = forms.CharField(widget=TextInput(attrs={'placeholder':'confirm password...'}), required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Bu email avval ro\'yxatdan o\'tgan, iltimos boshqa email kiriting:')
        return email
    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if password1 != password2:
            raise forms.ValidationError('Parollar bir-biriga mos emas!!!')
        return password2
    
    def save(self, commit=True):
        password = self.cleaned_data.get('password')
        user = super().save(commit)
        user.set_password(password)
        user.save()

        return user

class LoginForm(forms.Form):
    email = forms.EmailField(widget=EmailInput(attrs={'placeholder':'Emailingizni kiriting:'}), required=True)
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password kiriting:'}), required=True)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if not email or not password:
            raise forms.ValidationError('Bo\'sh bo\'lmasligi kerak!!!')
        return self.cleaned_data
    
class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone')




    
