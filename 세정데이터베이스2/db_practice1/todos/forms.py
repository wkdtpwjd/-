from django import forms
from .models import Todo
class TodoForm(forms.ModelForm):
    completed = forms.BooleanField(
        required=False,
        widget= forms.CheckboxInput(attrs={'class':'completed'})
    )
    class Meta:
        model = Todo
        fields = ('content','completed')
        