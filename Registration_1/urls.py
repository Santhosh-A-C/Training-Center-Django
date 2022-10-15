from django.urls import re_path
from Registration_1 import views

urlpatterns = [
    re_path(r'^$',views.index,name='index'),

]