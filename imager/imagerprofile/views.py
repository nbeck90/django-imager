from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from imager_images.models import ImagerPhoto, ImagerAlbum, User
from django.views.generic import UpdateView
from imagerprofile.models import ImagerProfile
from imagerprofile.forms import UserProfileForm


class ImagerProfileUpdateView(UpdateView):
    model = ImagerProfile
    template_name_suffix = '_update_form'
    form_class = UserProfileForm
    context_object_name = 'profile'
    success_url = '/profile/'
    # fields = [
    #     'profile_picture',
    #     'phone_number',
    #     'birthday',
    #     'phone_privacy',
    #     'birthday_privacy',
    #     'picture_privacy',
    #     'name_privacy',
    #     'email_privacy',
    #     'following',
    #     'blocking',
    # ]

    def get_queryset(self):
        qs = super(ImagerProfileUpdateView, self).get_queryset()
        return qs.filter(user=self.request.user)

    def get_initial(self):
        initial = super(ImagerProfileUpdateView, self).get_initial()
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        initial['email'] = self.request.user.email
        return initial

    def form_valid(self, form):
        # import pdb; pdb.set_trace()
        user = form.instance.user
        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.email = form.cleaned_data.get('email')
        user.save()
        return super(ImagerProfileUpdateView, self).form_valid(form)

    # def get_form_kwargs(self):
    #     import pdb; pdb.set_trace()
    #     return super(ImagerProfileUpdateView, self).get_form_kwargs()


@login_required()
def profile(request):
    user = request.user
    try:
        albums = ImagerAlbum.objects.filter(user=user).all()
    except:
        albums = None
    profile = ImagerProfile.objects.get(user=user)
    following = len(profile.followers.all())
    num_photos = ImagerPhoto.objects.filter(user=user).count()
    return render(request, 'profile.html', {
        'albums': albums,
        'user': user,
        'profile': profile,
        'following': following,
        'num_photo': num_photos
    })


@login_required()
def user_profile(request, id):
    user = User.objects.get(id=id)
    try:
        albums = ImagerAlbum.objects.filter(user=user).all()
    except:
        albums = None
    profile = ImagerProfile.objects.get(user=user)
    following = len(profile.followers.all())
    num_photos = ImagerPhoto.objects.filter(user=user).count()
    return render(request, 'user_profile.html', {
        'albums': albums,
        'user': user,
        'profile': profile,
        'following': following,
        'num_photo': num_photos
    })


@login_required()
def library(request):
    user = request.user
    try:
        albums = ImagerAlbum.objects.filter(user=user).all()
    except:
        albums = None
    try:
        photos = ImagerPhoto.objects.filter(user=user).all()
    except:
        photos = None
    return render(request, 'library.html', {
        'user': user,
        'albums': albums,
        'photos': photos
    })


@login_required()
def stream(request):
    user = request.user
    try:
        my_albums = request.user.albums.filter(user=user).all()
    except:
        my_albums = None
    try:
        followed_albums = ImagerAlbum.objects.filter(user=user.profile.is_following()).all()
    except:
        followed_albums = None
    try:
        photos = ImagerPhoto.objects.filter(user=user).all()
    except:
        photos = None
    try:
        followed_photos = ImagerPhoto.objects.filter(user=user.profile.is_following()).all()
    except:
        followed_photos = None
    return render(request, 'stream.html', {
        'user': user,
        'my_albums': my_albums.order_by('-date_created'),
        'followed_albums': followed_albums.order_by('-date_created'),
        'photos': photos.order_by('-date_uploaded'),
        'followed_photos': followed_photos.order_by('-date_uploaded'),
    })
