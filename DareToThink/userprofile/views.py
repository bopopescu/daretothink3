from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from userprofile.forms import UserForm, UserProfileForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from userprofile.models import UserProfile
from django.contrib.auth.models import Group

from allauth.account.signals import user_signed_up, email_confirmed
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress


#---REGISTER----------------------------------------------------------------------

def userprofile_register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.

        data_with_username = request.POST
        data_with_username['username'] = data_with_username['email']
        user_form = UserForm(data=data_with_username)
        profile_form = UserProfileForm(data=data_with_username)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.is_staff = True

            #my stuff

            #g = Group.objects.get(name='normal_users')
            #g.user_set.add(user)


            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            user_form.errors, profile_form.errors
            #CHECK: had print next to above line

    #------------ log em in---

        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)

    #-------------------------

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()


    # Render the template depending on the context.
    return render_to_response(
            'userprofile_register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)


    #---LOG IN------------------------------------------------------

def userprofile_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']
        #password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                Redirect_Url = '/' + user.first_name + user.last_name + '/'
                return HttpResponseRedirect(Redirect_Url)
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            "Invalid login details: {0}, {1}".format(username, password)
            #CHECK: was print before above line
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('userprofile_login.html', {}, context)

    #---LOG OUT------------------------------------------------------


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def userprofile_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('')

    #----PROFILE ------------------------------------------------------


@login_required
def userprofile_index(request):
    #context = RequestContext(request)
    u = User.objects.get(username=request.user)

    try:
        up = UserProfile.objects.get(user=u)
    except:
        up = None

    context_dict = {}
    context_dict['user'] = u
    context_dict['userprofile'] = up
    #return render_to_response('userprofile_index.html', context_dict, context)
    return render(request, 'userprofile_index.html', context_dict)

#----ALLAUTH-------------------------------------

@receiver(user_signed_up)
def user_signed_up_(request, user, **kwargs):

    user.is_staff = True
    Group.objects.get(name='normal_users').user_set.add(user)

    user.save()
