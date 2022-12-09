from django.urls import path
from . import views

urlpatterns = [
    path('',views.counter),
    path('addvisit',views.addvisit),
    path('show',views.show),
    path('reset',views.reset),
    path('result',views.reresult)

]