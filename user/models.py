from django.db import models

# Create your models here.

class User(models.Model):
    CENDERS = (
        ('male','男性'),
        ('female','女性'),
    )
    LOCATIONS = (
        ('北京','北京'),
        ('上海','上海'),
        ('广州','广州'),
        ('深圳','深圳'),
        ('成都','成都'),
        ('武汉','武汉'),
        ('洛阳','洛阳')
    )


    phonenum = models.CharField(max_length=16,verbose_name='手机号')
    nickname = models.CharField(max_length=20,verbose_name='昵称')
    gender = models.CharField(max_length=10,choices=CENDERS,verbose_name='性别')
    birthday = models.DateTimeField(default='2002-01-01',verbose_name='出生日')
    avatar = models.CharField(max_length=256,verbose_name='个人形象')
    location = models.CharField(max_length=10,choices=LOCATIONS,verbose_name='常居地')

    def to_dict(self):
        return{
            'id':self.id,
            'phonenum':self.phonenum,
            'nickname':self.nickname,
            'gender':self.gender,
            'birthday':self.birthday,
            'avatar':self.avatar,
            'location':self.location,
        }

