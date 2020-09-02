from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')), 
    url(r'^memories/$', views.CreateView.as_view(), name="create"),
    url(r'^memories/(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name="details"),
    url(r'^users/$', views.UserView.as_view(), name="users"),
    url(r'users/(?P<pk>[0-9]+)/$', views.UserDetailsView.as_view(), name="user_details"),
    url(r'^get-token/', obtain_auth_token),
    url(r'^$', views.Home, name="home"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
