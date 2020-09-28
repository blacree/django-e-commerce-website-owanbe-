from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'loginsignup'

urlpatterns = [
    path('login1', LoginView.as_view(template_name='login.html'), name='loginpage1' ),
    path('login', views.userlogin, name='loginpage2'),
    path('login2', views.log_in, name='loginpage3'),
    path('signup', views.signup, name='signup'),
    path('test', views.testdiff, name='test'),
    path('logout', views.logout_view, name='logout'),
    #path('signup2', views.signup2, name='signup2'),
    #path('signup3', views.signup3, name='signup3')
]