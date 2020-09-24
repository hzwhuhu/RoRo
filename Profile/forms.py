from django import forms

from Profile.models import Profile
from user.models import User

class UserForm(forms.ModelForm):

    class Meta:
        model=User
        fields = ['nickname','gender','birthday','location']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'

    def clean_max_distance(self):
        cleaned_data=super().clean()
        if cleaned_data['max_distance'] < cleaned_data['min_distance']:
            raise forms.ValidationError('最大距离必须大于最小距离')
        else:
            return cleaned_data['max_distance']
    def clean_max_dating_age(self):
        cleaned_data=super().clean()
        if cleaned_data['max_dating_ag'] < cleaned_data['min_dating_ag']:
            raise forms.ValidationError('最大交友年龄必须大于最小交流年龄')
        else:
            return cleaned_data['max_dating_ag']