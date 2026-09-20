from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll_no', 'name', 'email', 'age', 'course',
                  'marks', 'phone', 'address', 'is_active']
        widgets = {
            'roll_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 22edics001'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'student@email.com'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'min': 15, 'max': 60}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'marks': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': 0, 'max': 100}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '10-digit number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_marks(self):
        marks = self.cleaned_data.get('marks')
        if marks is not None and (marks < 0 or marks > 100):
            raise forms.ValidationError("Marks 0 se 100 ke beech hone chahiye!")
        return marks

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 15 or age > 60:
            raise forms.ValidationError("Age 15 se 60 ke beech honi chahiye!")
        return age