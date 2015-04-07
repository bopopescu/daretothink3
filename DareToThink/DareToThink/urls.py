from django.conf.urls import patterns, include, url
from DareToThink.views import index
from userprofile.views import userprofile_register, userprofile_login, userprofile_logout
from userprofile.viewsblog import userprofile_blog, userprofile_newblog
from userprofile.viewsprofile import userprofile_profile
from django.contrib import admin
from django.views.generic import TemplateView
from DareToThink.settings import MEDIA_ROOT
from filebrowser.sites import site



admin.autodiscover()
urlpatterns = patterns('',
url(r'^admin/', include(admin.site.urls), name='admin'),
url(r'^admin/filebrowser/', include(site.urls)),
url(r'^grappelli/', include('grappelli.urls')),
url(r'^accounts/', include('allauth.urls')),
url(r'^tinymce/', include('tinymce.urls')),
#url(r'^summernote/', include('django_summernote.urls')),
url(r'^$', index.as_view(), name='indextemplate'),
url(r'^about/', TemplateView.as_view(template_name="about.html"), name='about'),
#url(r'^AdminProfile/', include(AdminProfile.urls), name='AdminProfile'),
url(r'^register/$', userprofile_register, name='userprofile_register'),
url(r'^login/$', userprofile_login, name='userprofile_login'),
url(r'^logout/$', userprofile_logout, name='userprofile_logout'),
url(r'^blog/', userprofile_blog, name='userprofile_blog'),
url(r'^newblog/', userprofile_newblog, name='userprofile_newblog'),
url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
#url(r'^profile/$', userprofile_profile, name='userprofile_profile'),
#url(r'^(?P<user1>\w+)', userprofile_profile, name='userprofile_profile'), # Keep at the bottom so any /requests go here
)

