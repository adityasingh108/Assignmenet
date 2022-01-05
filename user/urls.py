from django.urls import path
from . views import PostList,PostDetail,PostCreate, PostUpdate,DeleteView,CustomLoginView,RegisterPage
from django.contrib.auth.views import  LogoutView
urlpatterns = [
    
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page = 'login'), name="logout"),
    path("register/", RegisterPage.as_view(), name="register"),
    
    
    path('post/',PostList.as_view(),name='post'),
    path('post_detail/<int:pk>/',PostDetail.as_view(),name='post_detail'),
    path('post-create/',PostCreate.as_view(),name='post-create'),
    path('post-update/<int:pk>/',PostUpdate.as_view(),name='post-update'),
    path('post-delete/<int:pk>/',DeleteView.as_view(),name='post-delete'),
    
    
]
   