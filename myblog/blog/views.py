import markdown

from django.shortcuts import render, get_object_or_404
from comments.forms import CommentForm
from .models import Article, Category
# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from .models import Article, Category
# import markdown
# from ..comments.forms import CommentForm
# Create your views here.


# 主页
def index(request):
    article_list = Article.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'article_list': article_list})


# 详情页
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 'markdown.extensions.extra':包含很多语法拓展
    # 'markdown.extensions.codehilite': 语法高亮扩展
    # 注: 实现代码高亮还需要两步,第一步如上,第二步安装第三方包pygments,第三步导入样式表文件,见base.html
    # 'markdown.extensions.toc': 自动生成目录
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])
    form = CommentForm()
    comment_list = article.comment_set.all()
    context = {
        "article": article,
        "form": form,
        "comment_list": comment_list,
    }
    return render(request, 'blog/detail.html', context=context)


# 归档功能
def archives(request, year, month):
    article_list = Article.objects.filter(created_time__year=year,
                                          created_time__month=month
                                          ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'article_list': article_list})


# 分类功能
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    article_list = Article.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'article_list': article_list})