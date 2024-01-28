from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name='index'),
    path('main-manager/list',views.mainMainagerList,name='mmlist'),

]
