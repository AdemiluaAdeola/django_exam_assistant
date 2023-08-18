from django.urls import path
from auth_app.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterView.as_view(), name='register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='update_profile'),
    path('profile/', UserProfileView.as_view(), name="profile"),
]