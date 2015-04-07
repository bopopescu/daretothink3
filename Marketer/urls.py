from django.conf.urls import patterns, include, url
from views import index_main
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

#url(r'^$', TemplateView.as_view(template_name="index_main.html"), name='index_main'),
url(r'^$', index_main, name='index_main'),
)
