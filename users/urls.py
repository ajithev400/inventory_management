from django.urls import path
from .views import ObtainTokenAPIView, RefreshTokenAPIView,UserView,CreateUserView

urlpatterns = [
    path('token/', ObtainTokenAPIView.as_view(), name='obtain_token'),
    path('token/refresh/', RefreshTokenAPIView.as_view(), name='refresh_token'),

    path('', UserView.as_view()), 
    path('<int:user_id>/', UserView.as_view()),
    path('create/', CreateUserView.as_view()), 
]