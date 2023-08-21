from django.urls import path
from app import views

# url patterns

urlpatterns = [
    path('',views.login,name='login'),                      # user login page
    path('index/',views.index,name='index'),               #home page (user page)
    path('signUp/',views.signUp,name='signUp'),             # sign up page
    path('adminLog/',views.adminLog,name='adminLog'),
    #path('logout/',views.logout,name='logout'),
]
