from django.urls import path
from . import views
from django.conf.urls import url 

urlpatterns = [path("", views.home, name="home"),
                path('cust', views.cust, name="cust"),
                path('trans', views.trans, name="trans"),
                path('transaction',views.transaction,name="transaction"),

                
              
]