from django.urls import path
from . import views


urlpatterns = [
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('addchildren/',views.addChildren, name = "addChildren"),
    path('profile/<int:code>/', views.ChildProfile, name='ChildProfile'),
    path('EditChildren/<int:code>/',views.EditChildren, name='EditChildren'),
    path('EducationProfile/',views.EducationProfile, name='EducationProfile'),
    path('SponsorProfile/',views.SponsorProfile, name='SponsorProfile'),
    path('check/',views.Check, name='Check'),
	path('demo/',views.demo,name='demo')
]
