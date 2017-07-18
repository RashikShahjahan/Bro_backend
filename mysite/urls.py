#mysite URL Configuration

from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from nlp_core import views

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^data/', views.DataList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
