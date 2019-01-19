from django.conf.urls import url

from blog import views

app_name = "blog"

urlpatterns = [
    url(r"^$", views.homepage, name="homepage"),
    url(r"post/(\w+)$", views.show_post, name="show_post"),
    url(r"^add", views.add, name="add"),
    url(r"^ajax$", views.ajax_dict, name="ajax"),
    url(r"^ajax_2", views.add, name="ajax_2"),
]
