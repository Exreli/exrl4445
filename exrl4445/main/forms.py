from django import forms


class ExtraArgumentForm(forms.Form):
    extra = forms.CharField()
