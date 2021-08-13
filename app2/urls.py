from django.urls import path
from app2 import views
app_name='archi'


urlpatterns = [

    path('art/',views.archi,name='art'),
]