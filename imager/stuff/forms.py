from django import forms
from imagerprofile.models import ImagerProfile
# from imager_images.models import User


# class UserProfileForm(forms.ModelForm):
#     first_name = forms.CharField(label='First Name', max_length=30)
#     last_name = forms.CharField(label='Last Name', max_length=30)
#     email = forms.EmailField(label='Email', max_length=30)

#     def __init__(self, *args, **kw):
#         super(UserProfileForm, self).__init__(*args, **kw)
#         self.fields['first_name'].initial = self.instance.user.first_name
#         self.fields['last_name'].initial = self.instance.user.last_name
#         self.fields['email'].initial = self.instance.user.email

#     def save(self, *args, **kw):
#         super(UserProfileForm, self).save(*args, **kw)
#         self.instance.user.first_name = self.cleaned_data.get('first_name')
#         self.instance.user.last_name = self.cleaned_data.get('last_name')
#         self.instance.user.email = self.cleaned_data.get('email')
#         self.instance.user.save()

#     class Meta:
#         model = ImagerProfile
#         exclude = ('user',)
#         fields = [
#             'first_name',
#             'last_name',
#             'email',
#             'profile_picture',
#             'phone_number',
#             'birthday',
#             'phone_privacy',
#             'birthday_privacy',
#             'picture_privacy',
#             'name_privacy',
#             'email_privacy',
#             'following',
#             'blocking',
#         ]
