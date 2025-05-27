from django.contrib import admin
from django.urls import path
from apps.Users.views import RegisterUserView, CreateSuperUserAPIView, LoginView, LogoutView
from apps.MediaList.views import SaveMedia, SearchMediaByActors, SearchMediaByTitle
from apps.Reviews.views import CreateReview, DeleteReview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/register_user/', RegisterUserView.as_view(),name='api/register_user'),
    path('api/register_superuser/', CreateSuperUserAPIView.as_view(),name='api/register_superuser'),
    path('api/save_media/', SaveMedia.as_view(),name='api/save_media'),
    path('api/search_by_actor/', SearchMediaByActors.as_view(),name='api/search_by_actor'),
    path('api/search_by_title/', SearchMediaByTitle.as_view(),name='api/search_by_title'),
    path('api/create_review/', CreateReview.as_view(),name='api/createreview'),
    path('api/delete_review/', DeleteReview.as_view(),name='api/deletereview'),
]
