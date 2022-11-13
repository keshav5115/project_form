from django.urls import path
from app1 import views
app_name='app1'
urlpatterns=[
    path('register/',views.studentview,name='register'),
    path('read/',views.read,name='read'),
    path('update/',views.update,name='update'),
    path('update_value/<sid>/',views.update_value,name='update_value'),
]