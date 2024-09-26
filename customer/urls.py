from django.urls import path
from .views import *


urlpatterns = [
    path('index/',indexpage),
    path('about/',aboutpage),
    # path('customerlist/',customerlist),
    # path('customeradd/',customeradd),
    # path('customerupdate/<int:id>/',customerupdate,name= 'cus_update'),
    # path('customerdelete/<int:id>/',customerdelete,name= 'cus_delete'),

    path('customeradd/',CustomerAddView.as_view()),
    path('customerlist/',CustomerListView.as_view()),
    path('customerupdate/<int:id>/',CustomerUpdateView.as_view(),name= 'cus_update'),
    path('customerdelete/<int:id>/',CustomerDeleteView.as_view(),name= 'cus_delete'),

    
]