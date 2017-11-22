from django.conf.urls import url
from . import views


app_name ='personal_space'

urlpatterns = [
    #/personal_space/
    url(r'^$', views.Indexview.as_view(), name='index'),
    #/personal_space/topic__id
    url(r'^(?P<pk>[0-9]+)/$', views.Detailview.as_view(), name='detail'),
    #/personal_space/topic_id/delete_topic/
    url(r'^(?P<pk>[0-9]+)/delete_topic/$', views.Delete_topic.as_view(), name='delete_topic'),
    #/personal_space/topic/add
    url(r'^topic/add/$', views.TopicCreate.as_view(), name='create_topic'),
    #/personal_space/topic_id/update
    url(r'^(?P<pk>[0-9]+)/update/$', views.TopicUpdate.as_view(), name='update_topic'),

]
