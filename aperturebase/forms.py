from django import forms

class ContactForM(forms.Form):
    Name = forms.CharField(label='Name',max_length=100)
    sender = forms.EmailField(label='Email')
    
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
