from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video_file', 'thumbnail']



from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

