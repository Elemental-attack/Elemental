from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.
from matrix.models import Technique, Note
from django import forms

class noteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('technique', 'note', 'date')
    

