# 语言及时区设置
  - LANGUAGE_CODE = 'zh-hans'
  - TIME_ZONE = 'Asia/Shanghai'
# 数据库结构设计
文章id	标题	 正文	 发表时间	分类	  标签
  1	   title 1	body 1	2016-12-23	Django	Django学习
  2	   title 2	body 2	2016-12-24	Django	Django学习
  3	   title 3	body 3	2016-12-26	Python	Python学习
-----------------------改良如下-----------------------
表一:
文章id  标题     正文
  1    title 1  body 1
  2    title 2  body 2
  3    title 3  body 3
表二:
分类id  分类名
  1     Django
  2     Python
表三:
标签id  标签名
  1     Django学习
  2     Python学习
## 表一和表二建立一对多关系
文章id	标题	正文	分类id
  1	   title 1	body 1	  1
  2	   title 2	body 2	  1
  3	   title 3	body 3	  1
  4	   title 4	body 4	  2
分类id	分类名	
  1	    Django	
  2	    Python
- 注: 可见表一和表二可以通过[分类id]建立起联系
## 表一和表三建立多对多关系
文章id	标题	正文
  1	   title 1	body 1
  2	   title 2	body 2
  3	   title 3	body 3
  4	   title 4	body 4
标签id	标签名
  1	    Django学习
  2	    Python学习
文章id	标签id
  1	      1
  1 	  2
  2	      1
  3 	  2 
- 注: 可见表一和表三无法向表一和表二那样通过添加一列[分类id]建立联系,而是需要额外的一张表由[文章id]和[标签id]两列构成来
      建立联系;[文章id]=1可找到两个标签,[标签id]=1可找到两篇文章
# 迁移数据库
python manage.py sqlmigrate blog 0001: 查看对应的数据库语言,有助于理解Django ORM的工作机制
# MarkDown参考资料
- [http://www.jianshu.com/p/1e402922ee32/]
- [http://www.appinn.com/markdown/]      	
# safe标签: 过滤器
Django出于安全方面的考虑,任何的HTML代码在Django的模板中都会被转义(即显示原始的HTML代码,而不是经浏览器渲染后的格式).
为了解除转义，只需在模板标签使用 safe 过滤器即可，告诉 Django，这段文本是安全的，你什么也不用做。
在模板中找到展示博客文章主体的 {{ article.body }} 部分，为其加上 safe 过滤器，{{ article.body|safe }}
# 归档功能最后需要导入pytz第三方包
  
  
