from django.urls import path

app_name='app2'

from app2 import views
urlpatterns=[
path('create/',views.create,name='create'),
path('update/',views.update,name='update'),
path('updaterecord/ ',views.updaterecord,name='updaterecord'),
]