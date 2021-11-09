from django.urls import path
from django.views.generic.base import TemplateView

from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('proxy/<path:url>', LocalProxy.as_view(), name='proxy'),
    # url(r'^proxy/(?P<url>.*)$', reverse_proxy, name='proxy'),
]
