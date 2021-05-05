from django.conf.urls import url
from django.urls import path
from params import views

urlpatterns = [
    path('', views.testcase_list, name="testcase_list"),
    path('<int:test_id>/test/', views.testcase_detail),
    path('runscript/', views.runscript_list),
    path('<str:key>/runscript/', views.runscript_detail),
]
