from django import forms
from .models import Submission
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ('eid', 'document')
