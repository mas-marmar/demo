from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from . import views

urlpatterns = [
    path('', views.CourseListView.as_view(), name='main'),
    
    path('login/', LoginView.as_view(template_name='login.html', success_url=reverse_lazy('main')), name='login'),
    path('logout/', LogoutView.as_view(next_page='main'), name='logout'),
    path('register/', views.MyRegistrationView.as_view(), name='register'),
    
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('create-request/', views.CreateRequestView.as_view(), name='create_request'),
]