from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
# 导入兼容python2的装饰器
# from django.utils.six import python_2_unicode_compatible


# @python_2_unicode_compatible
class Category(models.Model):
    # category: n.种类,分类
    name = models.CharField(max_length=100)

    objects = models.Manager()

    # 1.如果是python2环境,则需要使用装饰器,导入,使用语法糖
    # 2.如果不想使用装饰器,只需使用__unicode__方法替代__str__
    def __str__(self):
        return self.name


class Tag(models.Model):
    # tag: n.标签
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    # article:文章
    # article的标题和文章主题
    # 存储较短的字符串可以使用charfield,存储长文本可使用textfield
    title = models.CharField(max_length=70)
    body = models.TextField()

    # article创建时间和最后一次修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # article的摘要,允许空值
    excerpt = models.CharField(max_length=200, blank=True)

    # 1.article和category建立联系
    # 一篇文章只属于一个分类,一个分类可以有多篇文章,一对多关系
    # 故使用ForeignKey建立联系
    # 2.article和tag建立联系
    # 一篇文章可以有多个标签,一个标签可以有多篇文章,多对多关系
    # 故使用ManyToMany建立联系
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    # django.contrib.auth: django内置应用, 专门用于处理网站用户的注册登录等流程, User是已经写好的用户模型
    # 一篇文章一个作者,一个作者多篇文章, 一对多关系, 使用ForeignKey
    # 注: 在创建article之间,先创建User-->python manage.py createsuperuser
    author =models.ForeignKey(User)

    objects = models.Manager()

    def get_absolute_url(self):
        # 解析url
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
