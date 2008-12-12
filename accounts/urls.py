from django.conf.urls.defaults import *
from django.contrib.auth import auth_views

from accounts.views import edit

urlpatterns = patterns('',
    url(r'^login/$', auth_views.login, name='auth_login'),
    url(r'^logout/$', auth_views.logout, name='auth_logout'),
    url(r'^password/change/$', auth_views.password_change, {
        'template_name': 'accounts/password_change_form.html'
    }, name='auth_password_change'),
    url(r'^password/change/done/$', auth_views.password_change_done, {
        'template_name': 'accounts/password_change_done.html'
    }, name='auth_password_change_done'),
    url(r'^edit/$', edit, name='accounts_edit'),
)
