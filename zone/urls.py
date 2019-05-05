from django.urls import path
from . import views


urlpatterns=[
    path('main/', views.main, name="main"),
    path('intro/', views.intro, name="intro"),
    path('babyinfo/', views.babyinfo, name="babyinfo"),
    path('commu/', views.commu, name="commu"),
    path('introo/', views.introo, name="introo"),
    path('notice/', views.notice, name="notice"),
    path('Q_A/', views.Q_A, name="Q_A"),
    path('create/', views.create, name="create"),
    path('milk/', views.milk, name="milk"),

    path('sick/', views.sick, name="sick"),
    path('board/', views.board, name="board"),
]

