from django.views.generic.create_update import update_object

from accounts.forms import EditUserForm

def edit(request, template_name='accounts/user_form.html'):
    return update_object(request, login_required=True, form_class=EditUserForm,
                         object_id=request.user.id, template_name=template_name)
