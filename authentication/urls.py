from django.urls import path
from .views import *


urlpatterns = [
    # path('',loginpage),
    # path('logout/',logoutpage),
    # path('signup/',signuppage),
    path('',AuthLoginpageView.as_view()),
    path('logout/',AuthLogoutpageView.as_view()),
    path('signup/',AuthSignuppageView.as_view())
]