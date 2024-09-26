from django.urls import path
from .views import *


urlpatterns = [
    path('home/',homepage),
    path('about/',aboutpage),


    path('productadd/',ProductAddView.as_view()),
    path('productlist/',ProductListView.as_view()),
    path('productupdate/<int:id>/',ProductUpdateView.as_view(),name= 'pro_update'),
    path('productdelete/<int:id>/',ProductDeleteView.as_view(),name= 'pro_delete'),



    
]

