from django.http import JsonResponse
from Profile.forms import UserForm, ProfileForm

from Profile.models import Profile


def show_profile(request):
    '''查看个人资料'''
    user_id = request.session.get('uid')
    profile,_=Profile.objects.get_or_create(id=user_id)
    return JsonResponse({'code': 0, 'data': profile.to_dict()})


def update_profile(request):
    '''更新个人资料'''
    user_form=UserForm(request.POST)
    profile_form=ProfileForm(request.POST)
    if user_form.is_valid() and profile_form.is_valid():
        uid = request.session.get['uid']
        User.objects.filter(id=uid).update(**user_form.cleaned_data)
        Profile.objects.update_or_create(id=uid,defaults=profile_form.cleaned_data)
        return JsonResponse({'code':0,'data':None})
    else:
        err={}
        err.update(user_form.errors)
        err.update(profile_form.errors)
        return JsonResponse({'code':1003,'data':err})


