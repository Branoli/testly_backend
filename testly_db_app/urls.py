from django.conf.urls import url
from testly_db_app import views


urlpatterns = [
    url(r'^db/get$', views.get_all),
    url(r'^db/post$', views.post_element),
    url(r'^db/get_subtree/(?P<pk>[0-9]+)/', views.get_subtree),
    url(r'^db/search/(?P<text>[a-zA-Zа-яА-я]+)/$', views.get_search_text),
]