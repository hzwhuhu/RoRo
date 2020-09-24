from django.core.cache import cache
from django.http import JsonResponse

from user.logics import send_vcode
from user.models import User
from libs.qn_cloud import gen_token
from libs.qn_cloud import get_res_url

# Create your views here.



def fetch_vcode(request):
    '''给用户发送验证码'''
    phonenum = request.GET.get('phonenum')
    if send_vcode(phonenum):
        return JsonResponse({'code': 0, 'data': None})
    else:
        return JsonResponse({'code': 1000, 'data': '验证码发送失败'})


def submit_vcode(request):
    '''提交验证码，执行登录注册'''
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')

    key = 'Vcode-%s' % phonenum
    cached_vcode = cache.get(key)

    if vcode and vcode == cached_vcode:
        try:
            user = User.objects.get(phonenum=phonenum)  # 从数据库获取用户
        except User.DoesNotExist:
            # 如果用户不存在，则执行注册流程
            user = User.objects.create(phonenum=phonenum, nickname=phonenum)

        # 在 Session 中记录用户登录的状态
        request.session['uid'] = user.id

        return JsonResponse({'code': 0, 'data': user.to_dict()})
    else:
        return JsonResponse({'code': 1001, 'data': '验证码错误'})


def qn_token(request):
    '''获取七牛云'''
    uid = request.session['uid']
    filename = f'Avatar-{uid}'
    token = gen_token(uid,filename)
    return JsonResponse({
        'code': 0,
        'data': {
            'token': token,
            'key': filename,
        }
    })


def qn_callback(request):
    uid = request.POST.get('uid')
    key = request.POST.get('key')
    avatar_url = get_res_url(key)
    User.objects.filter(id=uid).update(avatar=avatar_url)
    return JsonResponse({
        'code': 0,
        'data': avatar_url
    })