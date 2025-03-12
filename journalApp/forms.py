from django import forms
from .models import Entry

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'caption']  # Add your actual model fields