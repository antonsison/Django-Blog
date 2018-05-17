from django.urls import path, re_path

from . import views

app_name = 'posts'
urlpatterns = [
	path('', views.post_list, name='list'),
	path('create/', views.post_create, name='create'),
	path('about/', views.post_about, name='about'),
	re_path(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='detail'),
	re_path(r'^(?P<slug>[\w-]+)/edit/$', views.post_update, name='update'),
	re_path(r'^(?P<slug>[\w-]+)/delete/$', views.post_delete, name='delete'),
	

]
