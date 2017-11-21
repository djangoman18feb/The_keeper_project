from django.conf.urls import url
from . import views


app_name ='personal_space'

urlpatterns = [
    #/personal_space/
    url(r'^$', views.index, name='index'),
    #/personal_space/topic__id
    url(r'^(?P<topic_id>[0-9]+)/$', views.detail, name='detail'),





]
