from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
app_name = 'Post'
from Post import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^api/record/$', views.RecordList.as_view()),
    # url(r'^record/(?P<singer_name>\w+)/$', views.RecordDetail.as_view()),
    url(r'^search/$', views.search),
    url(r'^update/$', views.update),
    url(r'^hot/$', views.hot, name="hot"),
    url(r'^api/hot/$', views.HotList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)