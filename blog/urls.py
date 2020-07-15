from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('detail/<int:post_id>/', views.post_detail, name='detail'),
    path('new_post',views.new_post,name='new_post'),
    path('update_post/<slug:id>/', views.update_post, name='update_post'),
    # path('delete_post',views.delete_post,name='delete_post'),
    path('delete_post/<slug:id>/', views.delete_post, name='delete_post'),

]
