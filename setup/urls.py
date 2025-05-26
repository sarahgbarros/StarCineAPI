from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.Users.views import RegisterUserView, CreateSuperUserAPIView
from apps.MediaList.views import SaveMedia, SearchMediaByActors, SearchMediaByTitle

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register_user/', RegisterUserView.as_view(),name='api/register_user'),
    path('api/register_superuser/', CreateSuperUserAPIView.as_view(),name='api/register_superuser'),
    path('api/save_media/', SaveMedia.as_view(),name='api/save_media'),
    path('api/search_by_actor/', SearchMediaByActors.as_view(),name='api/search_by_actor'),
    path('api/search_by_title/', SearchMediaByTitle.as_view(),name='api/search_by_title'),
]
