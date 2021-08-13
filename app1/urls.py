from django.urls import path
from app1 import views
app_name='amit'

urlpatterns = [

    path('amt/',views.amit,name='amt'),
]