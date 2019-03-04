from django.forms import ModelForm
from core1.models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields=['first_name','department','designation']
