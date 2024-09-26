from django.urls import path
from .views import *


urlpatterns = [
    # path('orderadd/',orderadd),
    # path('orderlist/',orderlist),
    # path('orderupdate/<int:id>/',orderupdate,name= 'ord_update'),
    # path('orderdelete/<int:id>/',orderdelete,name= 'ord_delete'),

    path('orderadd/',OrderAddView.as_view()),
    path('orderlist/',OrderListView.as_view()),
    path('orderupdate/<int:id>/',OrederUpdateView.as_view(),name= 'ord_update'),
    path('orderdelete/<int:id>/',OrderDeleteView.as_view(),name= 'ord_delete'),



]