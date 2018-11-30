from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import include, path

from accounts import views as account_views

app_name = 'accounts'

urlpatterns = [

    url(r'^users_only/$',account_views.LoggedInView.as_view(),name='users_only'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^signup/$',account_views.SignUp,name='signup'),

    url(r'profile/(?P<username>[a-zA-Z0-9]+)/$', account_views.get_user_profile, name='user_profile'),
    # url(r'profile/(?P<slug>[-\w]+)$', account_views.get_user_profile, name='user_profile'),

    # url(r'profile/(?P<username>[a-zA-Z0-9]+)/user_update/$', account_views.UpdateProfile.as_view(), name='user_update'),
    url(r'profile/(?P<slug>[-\w]+)/user_update$', account_views.UpdateProfile.as_view(), name='user_update'),

    path(r'accounts/', include('django.contrib.auth.urls')),

    path(r'article_list', account_views.article_list),
    path(r'contact',account_views.js_contact,name='contact'),
        ]