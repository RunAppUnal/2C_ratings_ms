from django.conf.urls import url
from ratings import views


urlpatterns = [
    url(r'^ratings/$', views.rating_list),
    url(r'^ratings/(?P<pk>[0-9]+)/$', views.rating_detail),
]
