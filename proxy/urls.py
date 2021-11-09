from django.conf.urls import url
from django.urls import path
from django.views.generic.base import TemplateView

from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    url(r'^proxy/(?P<url>.*)$', reverse_proxy, name='proxy'),
]