from django import forms
class forminsert(forms.Form):
    project_number=forms.IntegerField()
    title=forms.CharField( )
    emp_id=forms.IntegerField(required=False)

from django import forms
class form_update(forms.Form):
    project_number=forms.IntegerField()
    title=forms.CharField( )
    emp_id=forms.IntegerField(required=False)