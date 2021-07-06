from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('signup', views.registerPage, name='signup'),
    path('write', views.write, name='write'),
    path('home', views.home, name='home'),
    path('story/<str:pk_story>/', views.story, name="story"),
    path('literacy', views.literacy, name='literacy'),
    path('genre/<str:pk_genre>/', views.genre, name="genre"),
]
