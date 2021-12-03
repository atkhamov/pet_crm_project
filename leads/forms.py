from django import forms
from .models import Lead

# Django's form.ModelForm has got more functionality then form.Form itself
# Therefore, it is advisable to use Django's build-in form.ModelForm
class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
        )


# class LeadForm(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     age = forms.IntegerField(min_value=0)
