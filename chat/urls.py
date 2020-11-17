from django.urls import path
from . import views

urlpatterns = [
    path('', views.discussionPage, name='discussionPage'),
    path('send/', views.sendPage, name='sendPage'),
    path('detail/<str:username>', views.detailPage, name='detailPage'),
    path('reply/<int:id>', views.replyPage, name='replyPage')
]
