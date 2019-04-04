from ..models import Article, Category
from django import template
# 1.自定义模板标签(实现特定功能的函数)
# 2.注册这个函数为模板标签
# 3.在模板中实用语法{% 函数名 %}调用函数
register = template.Library()


# 装饰器将函数装饰为simple_tag
@register.simple_tag
# 1.最新文章模板标签
def get_recent_articles(num=5):
    return Article.objects.all().order_by('-created_time')[:num]


@register.simple_tag
# 2.归档模板标签
def archives():
    '''
    dates方法返回一个list
    list中的元素是每一篇article的创建时间,且是python的date对象,精确到月份,降序排列
    三个参数: 第一个是article的创建时间,第二个是精度,第三个是排序方式
    例: 文章1: 2019.2.21; 文章2: 2019.3.23; 文章3: 2019.3.24
    返回包含2019.3和2019.2的一个时间列表,降序排列,实现按月归档的功能
    :return:
    '''
    return Article.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
# 3.分类模板标签
def get_categories():
    return Category.objects.all()