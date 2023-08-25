from django.urls import path
from app import views

# url patterns

urlpatterns = [
    path('',views.login,name='login'),                      # user login page
    path('index/',views.index,name='index'),               #home page (user page)
    path('signUp/',views.signUp,name='signUp'),             # sign up page
    path('adminLog/',views.adminLog,name='adminLog'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('admin_index/',views.admin_index,name='admin_index'),
    path('ad_create_user/',views.ad_create_user,name='ad_create_user'),
    path('logout_admin/',views.logout_admin,name='logout_admin'),
    path('ad_edit/<int:id>',views.ad_edit,name='ad_edit'),
    path('ad_delete/<int:id>',views.ad_delete_user,name='ad_delete'),
    path('admin_search/',views.admin_search,name='admin_search'),
]
