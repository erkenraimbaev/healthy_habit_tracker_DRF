from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.apps import UsersConfig
from users.views import MyTokenObtainPairView, UserListView, UserDetailView, UserCreateView, \
    UserUpdateView, UserDeleteView

app_name = UsersConfig.name

urlpatterns = [path('users/', UserListView.as_view(), name='users-list'),
               path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
               path('create/', UserCreateView.as_view(), name='users-create'),
               path('update/<int:pk>/', UserUpdateView.as_view(), name='users-update'),
               path('delete/<int:pk>/', UserDeleteView.as_view(), name='users-delete'),
               path('get_token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
               path('get_token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
               ]
