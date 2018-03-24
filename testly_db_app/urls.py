from django.conf.urls import url
from testly_db_app import views


urlpatterns = [
    url(r'^db/get$', views.get_all),
    ]