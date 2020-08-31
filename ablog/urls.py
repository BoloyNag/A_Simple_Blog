from django.urls import path
#from . import views
from . views import home_view, post_detail_view,add_post_view,update_post_view,delete_post_view,add_category_view

urlpatterns = [
    #path('', views.home,name="home"),
    path('',home_view.as_view(),name="home"),
    path('post/<int:pk>',post_detail_view.as_view(),name="post"),
    path('add_post/',add_post_view.as_view(),name="add_post"),
    path('post/edit/<int:pk>',update_post_view.as_view(),name="update_post"),
    path('post/<int:pk>/delete',delete_post_view.as_view(),name="delete_post"),
    path('add_category/',add_category_view.as_view(),name="add_category"),
]
