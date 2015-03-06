from django.contrib import admin
from imager_images.models import ImagerAlbum, ImagerPhoto
# from django.contrib.auth.admin import UserAdmin


# class ImagerAlbumInline(admin.StackedInline):
#     model = ImagerPhoto
#     verbose_name_plural = 'imager albums'


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('picture', 'title', 'user',
                    'description', 'date_modified')
    list_filter = ['albums', 'user']
    search_fields = ['title', 'albums', 'user']
    readonly_fields = ('image_tag', )


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'description',
                    'date_created', 'date_modified')
    list_filter = ['published', 'user']
    search_fields = ['title', 'published', 'user']
    # inlines = (ImagerAlbumInline, )


admin.site.register(ImagerAlbum, AlbumAdmin)
admin.site.register(ImagerPhoto, PhotoAdmin)
