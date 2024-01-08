from django import forms
from .models import ChatMessage
class UpdateProfileForm(forms.Form):
    fname = forms.CharField(max_length=25, required=True)
    lname = forms.CharField(max_length=25, required=True)
    email = forms.EmailField(required=True)
class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['message']