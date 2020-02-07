from django import forms
from django.core import validators

# def check_for_z(value):
#     if(value[0].lower() != 'z'):
#         raise forms.ValidationError("NAME NEEDS TO START WTIH Z")

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label = 'Enter your email again')
    text = forms.CharField(widget = forms.Textarea)
    # botcatcher = forms.CharField(required = False,validators=[validators.MaxLengthValidator(0)], widget=forms.HiddenInput)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        # vmail = email
        if (email != vmail):
            raise forms.ValidationError('holla hooooo')
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
 
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT")

    #     return botcatcher