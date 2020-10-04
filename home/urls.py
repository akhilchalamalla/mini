
from django.urls import path
from . import views
from . views import StorageListView,ReqListView,EventListView,Reqdetailview,AcceptView,RejectView
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',EventListView.as_view(), name='hom'),
    #path('login/',auth_views.LoginView.as_view(template_name="login.html"),name='login'),
    path('login/',views.login,name='login'),
    path('register',views.register,name='register'),
    

    path('home1',views.home1,name='home1'),
    path('logout',views.logout,name='logout'),
    path('eregister',views.eregister,name='eregister'),
    path('profile',views.profile,name='profile'),
    path('addevent',views.addevent,name='addevent'),
    path('registeredevents',StorageListView.as_view(),name='registeredevents'),
    path('reqevents',ReqListView.as_view(),name='reqevents'),
    path('requests/<int:pk>/',Reqdetailview.as_view(),name="reqdetail"),
    path('requests/<int:pk>/accept',AcceptView.as_view(),name="accept"),
    path('requests/<int:pk>/reject',RejectView.as_view(),name="reject"),
]
