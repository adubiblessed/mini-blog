from django.forms import ModelForm
from django import forms
from .models import User, Blog, Comment

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'rows': 4,
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'block w-full text-sm text-gray-700 file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'
            }),
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'blog_image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'rows': 5,
            }),
            'blog_image': forms.ClearableFileInput(attrs={
                'class': 'block w-full text-sm text-gray-700 file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'
            }),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'rows': 4,
            }),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username does not exist.")
        
        user = User.objects.get(username=username)
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect password.")
        
        return cleaned_data