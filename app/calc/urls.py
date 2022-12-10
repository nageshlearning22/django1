from django.urls import path

from . import views

urlpatterns= [
    path('',views.home,name='home'),
    path('template/',views.hometemplate,name='templates'),
    path('calculator/',views.telcalc),
    path('calculator/add/',views.add)
]