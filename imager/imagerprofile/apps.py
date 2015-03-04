from django.apps import AppConfig


class ImagerProfileConfig(AppConfig):

    name = 'imagerprofile'
    verbose_name = 'Imager Profile'

    def ready(self):
        from handlers import add_profile
