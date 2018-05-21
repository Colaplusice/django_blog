from mainsite import views

from django.conf.urls import url


app_name='mainsite'

urlpatterns = [
    url(r'^$',views.homepage,name='homepage'),
    url(r'post/(\w+)$',views.showpost,name='showpost'),
    url(r'^$',views.HomePage,name='Homepage'),
    url(r'^test_1$',views.test_1,name='test_1'),
    url(r'^test_2$',views.test_2,name='test_2'),
    url(r'^add',views.add,name='add'),
    url(r'^ajax$',views.ajax_dict,name='ajax'),
    url(r'^ajax_2',views.add,name='ajax_2'),
]