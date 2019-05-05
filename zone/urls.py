from django.urls import path
from . import views


urlpatterns=[
    path('main/', views.main, name="main"),
    path('intro/', views.intro, name="intro"),
    path('babyinfo/', views.babyinfo, name="babyinfo"),
    path('commu/', views.commu, name="commu"),
    path('notice/', views.notice, name="notice"),
    path('create/', views.create, name="create"),
    path('milk/', views.milk, name="milk"),
    path('show/<int:id>/', views.show, name="show"),
    path('sick/', views.sick, name="sick"),
    path('yet/', views.yet, name="yet"),
    path('board/', views.board, name="board"),
    path('notice_board/', views.notice_board, name="notice_board"),
    path('notice_detail/<int:id>/', views.notice_detail, name="notice_detail"),
    path('detail/<int:id>/', views.detail, name="detail"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('upd/<int:id>/', views.upd, name="upd"),
    path('dele/<int:id>/', views.dele, name="dele"),
    path('<int:id>/comment/', views.comment, name="comment"),
    path('<int:id>/co_create/', views.co_create, name="co_create"),
    path('<int:id>/co_show/', views.co_show, name="co_show"),
    path('mapp/', views.mapp, name="mapp"),
    path('<int:id>/co_update/', views.co_update, name="co_update"),
    path('<int:id>/co_delete/', views.co_delete, name="co_delete"),
]

