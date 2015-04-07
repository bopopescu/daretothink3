#from django.shortcuts import render
#from django.template import RequestContext
from django.views.generic import ListView
from userprofile.models import UserProfile
#from userprofile.forms import UserForm, UserProfileForm
#from userprofile.views import userprofile_register



#Class based index view--------------------------------
class index(ListView):
    model = UserProfile
    template_name = 'indextemplate.html'
    #register_all = userprofile_register.objects.all()

    def get_context_data(self, **kwargs):
        context = super(index, self).get_context_data(**kwargs)
        #context['userprofile_register'] = user_form
        #context['userprofile_register'] = userprofile_register.objects.all(),
        return context











# All models ----------------------------------
#allmodels_dict = {
#    "UserProfile" : UserProfile.objects.all(),
#}

#Deriving userprofile views--------------------------------
#def index(request):
#    context = userprofile_register(request)
#    return render(request, 'indextemplate.html', context)

