from django.conf.urls.defaults import *
from django.contrib.auth import views
from django.views.generic.create_update import update_object

from accounts.forms import EditUserForm

urlpatterns = patterns('',
    url(r'^login/$', views.login, name='auth_login'),
    url(r'^logout/$', views.logout, name='auth_logout'),
    url(r'^password/change/$', views.password_change, {
        'template_name': 'accounts/password_change_form.html'
    }, name='auth_password_change'),
    url(r'^password/change/done/$', views.password_change_done, {
        'template_name': 'accounts/password_change_done.html'
    }, name='auth_password_change_done'),
    url(r'^edit/(?P<object_id>\d+)/$', update_object, {
        'form_class': EditUserForm,
        'template_name': 'accounts/user_form.html',
    }, name='accounts_edit'),
)
