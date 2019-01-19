from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.template.loader import get_template

from .models import Post


def homepage(request):
    template = get_template('blog/index.html')
    posts = Post.objects.all()
    now = datetime.now()
    # local()函数代表将以上的变量加载html作为返回
    html = template.render(locals())
    return HttpResponse(html)


def show_post(request, slug):
    template = get_template("blog/post.html")
    post = Post.objects.get(slug=slug)
    if post is not None:
        # 得到内存中的数x
        html = template.render(locals())
        return HttpResponse(html)
    return redirect("/")


def add(request):
    a = range(100)
    return JsonResponse(a, safe=False)


def ajax_dict(request):
    name_dict = {"twz": "love python and django", "zqxt": "i am teaching Django"}
    return JsonResponse(name_dict)
