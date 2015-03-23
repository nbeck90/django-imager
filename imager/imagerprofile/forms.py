from django import forms
from imagerprofile.models import ImagerProfile


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    email = forms.EmailField(label='Email', max_length=30)

    class Meta:
        model = ImagerProfile
        fields = [
            'first_name',
            'last_name',
            'email',
            'profile_picture',
            'phone_number',
            'birthday',
            'phone_privacy',
            'birthday_privacy',
            'picture_privacy',
            'name_privacy',
            'email_privacy',
            'following',
            'blocking',
        ]
