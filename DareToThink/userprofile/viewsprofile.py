from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm, Textarea, TextInput
from django.contrib.auth.models import User
from userprofile.models import UserProfile

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name',]
        widgets = {
            #'title': TextInput(attrs={'cols': 70, 'rows': 1}),
            'email': TextInput(attrs={'class':'form-control',}),
            'first_name': TextInput(attrs={'class':'form-control',}),
            'last_name': TextInput(attrs={'class':'form-control',}),
        }

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['picture', 'location',]
        widgets = {
            #'title': TextInput(attrs={'cols': 70, 'rows': 1}),
            'location': TextInput(attrs={'class':'form-control',}),
            #'gender': TextInput(attrs={'class':'form-control',}),
            #'dateofbirth': TextInput(attrs={'class':'form-control',}),
        }

def userprofile_profile(request, user1):
    firstname = ""
    lastname = ""
    for x in user1:
        if x.istitle():
            y = user1.index(x)
            firstname = user1[:y]
            lastname = user1[y:]

    if request.user.is_anonymous():
        #ANONYMOUS
        url = 'userprofile_publicprofile.html'
    elif user1 == request.user.first_name + request.user.last_name:
        #REQUEST USER IS CHECKING HIS OWN PROFILE
        url = 'userprofile_profile.html'
        test = 'hello'
    else:
        #Not anonymous, and not request user, so must be another user logged in looking at a different profile
        url = 'userprofile_publicprofile.html'

    formdata = {}
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid(): #and userprofile_form.is_valid():
            user = User.objects.get(id=request.user.id)
            user_form = UserForm(request.POST, instance=user)

            formdata = request.POST #for pushing the new user data into context variable
            formdata['first_name'] = formdata['first_name'].title()
            formdata['last_name'] = formdata['last_name'].title()

            f2 = user_form.save(commit=False)
            f2.first_name = request.POST['first_name'].title()
            f2.last_name = request.POST['last_name'].title()
            user_form.save()
            if userprofile_form.is_valid():
                person, created = UserProfile.objects.get_or_create(user=request.user)
                if created:
                    userprofile_form = UserProfileForm(request.POST, request.FILES)
                    f = userprofile_form.save(commit=False)
                    if 'picture' in request.FILES:
                        file = request.FILES['picture']
                        f.picture = file.name
                    f.save()
                else:
                    userprofile_form = UserProfileForm(request.POST, request.FILES, instance=person)
                    f = userprofile_form.save(commit=False)
                    if 'picture' in request.FILES:
                        file = request.FILES['picture']
                        f.picture = file.name
                    f.save()


    user = User.objects.get(id=request.user.id)
    user_form = UserForm(instance=user)

    person, created = UserProfile.objects.get_or_create(user=request.user)
    if created:
        userprofile_form = UserProfileForm()
    else:
        userprofile_form = UserProfileForm(instance=person)

    template_data = {'userform' : user_form, 'userprofileform' : userprofile_form, 'formdata' : formdata,}
    return render(request, url, template_data)