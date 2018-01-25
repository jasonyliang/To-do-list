from django.contrib import admin
from django.conf.urls import url
from app1 import views
app_name = 'app1'
urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name='index'),
    # app1/ id number
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
]
