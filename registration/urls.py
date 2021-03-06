from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from registration import views

from . import views

app_name = "registration"


urlpatterns = [


    path('signup/', views.signup,name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('google-login', views.google_signin, name="google_signin"),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('choose-club', views.choose_club, name="choose-club")
]
