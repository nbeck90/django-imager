from django.apps import AppConfig


class ImagerProfileConfig(AppConfig):

    name = 'imagerprofile'
    verbose_name = 'Imager Profiles'

    def ready(self):
        import imagerprofile.handlers.add_profile
