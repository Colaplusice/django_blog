#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Post
import json
from datetime import datetime
from django.template.loader import get_template
#mainsite的内容
# Create your views here. 返回 post_lists
def HomePage(request):
    posts=Post.objects.all()
    post_lists=list()
    for count,post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count))+str(post)+"<br>")
        post_lists.append("<small>"+str(post.body.encode('utf8'))+"</small><br><br>")
    return HttpResponse(post_lists)
def homepage(request):
    print('调用了homepage函数')
    template=get_template('index.html')
    posts=Post.objects.all()
    now=datetime.now()
    #local()函数代表将以上的变量加载html作为返回
    html=template.render(locals())
    return HttpResponse(html)

def showpost(request,slug):
    print('调用了showpost函数')
    template=get_template('post.html')
    try:
        post=Post.objects.get(slug=slug)
        if post!=None:
                #得到内存中的数x
            html=template.render(locals())
            return HttpResponse(html)
    except:

        return redirect('/')


def test_1(request):

    return render(request,'test_1.html')


def test_2(request):
    print('suceesss')

    return HttpResponse('success')


def add(request):
    print('调用了add')
    a=range(100)
    return JsonResponse(a,safe=False)



def ajax_dict(request):
    print('sad')
    name_dict={'twz':'love python and django','zqxt':'i am teaching Django'}
    return JsonResponse(name_dict)


