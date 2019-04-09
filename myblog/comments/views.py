from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article

from .models import Comment
from .forms import CommentForm
# from django.shortcuts import render, get_object_or_404, redirect
# from ..blog.models import Article
# from .models import Comment
# from .forms import CommentForm
# Create your views here.


def article_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        # 用户提交的数据保存在了request.POST中,类字典对象
        form = CommentForm(request.POST)
        # 当调用is_valid()方法时,Django会自动检查表单数据是否符合格式要求
        if form.is_valid():
            # commit=False: 利用表单的数据生成Comment模型类的实例,并不保存到数据库
            comment = form.save(commit=False)
            # 将评论和被评论的文章关联起来
            comment.article = article
            # 保存数据到数据库
            comment.save()
            # 重定向到article的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的 URL。所以前提是:这个模型实例必须实现了get_absolute_url()方法
            return redirect(article)
        else:
            # article.comment_set.all()等价于comment.objects.filter(article=article)
            # 注: 这是一种简写方式,反向查询article实例的所有评论,另一种思路则是根据article筛选所有评论
            comment_list = article.comment_set.all()
            context = {
                'article': article,
                'form': form,
                'comment_list': comment_list,
            }
            return render(request, 'blog/detail.html', context=context)
    return redirect(article)