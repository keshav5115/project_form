from django.urls import path
from app3 import views
app_name='app3'
urlpatterns=[
 path('reg/',views.userview,name='reg'),
 path('login/',views.loginview,name='login'),
 path('homepage/',views.homepage,name='homepage'),
 path('logout/',views.logout_view, name='logout'),
]