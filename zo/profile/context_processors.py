from profile.forms import MyUserCreateForm

def create_form(request):
    return {'create_form': MyUserCreateForm()}