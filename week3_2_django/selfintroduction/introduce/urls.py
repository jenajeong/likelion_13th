from django.urls import path
from . import views

urlpatterns = [
    path('introduce/', views.introduce, name='introduce'),
] # 예약어라 변경 불가능한 name