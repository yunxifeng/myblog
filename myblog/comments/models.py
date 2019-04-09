from django.db import models

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    # 参数auto_now_add=True: 当评论保存到数据库时,自动把created_time的值指定为当前时间
    created_time = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('blog.Article')

    def __str__(self):
        return self.text[:20]
