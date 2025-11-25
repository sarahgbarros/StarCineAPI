from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from apps.Users.views import (
    RegisterUserView,
    CreateSuperUserAPIView,
    LoginView,
    LogoutView
)

from apps.MediaList.views import (
    SaveMedia,
    SearchMediaByTitle,
    ListAllMedia,
    DeleteMedia,
    UpdateMedia,
    FilterMediaByCategory,
    FilterMediaByGenre,
    FilterMediaByReleaseDate,
    FilterMediaByProductionStudio,
    FilterMediaByDirector,
    ListAllCategories,
    CreateCategory,
    DeleteCategory,
    UpdateCategory,
    DetailProductionInfo,
    CreateProductionInfo,
)

from apps.Reviews.views import (
    CreateReview,
    DeleteReview,
    UpdateReview,
    FilterReviewsByMedia,
    ListUserReviews,
    ListLatestReviews,
    ListTopRatedReviews,
    DetailReview,
    ListAllReviews,
    LikeReview
)

from apps.Lists.views import (
    SaveLists,
    DeleteLists,
    UpdateListCategory,
    CreateListCategory,
    DeleteListCategory,
    GetUserLists,
    AddMediaToList,
    RemoveMediaFromList
)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="StarCine API",
      default_version='v1',
      description="Api Swagger",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('swagger-json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/user/login/', LoginView.as_view(), name='login'),
    path('api/user/logout/', LogoutView.as_view(), name='logout'),
    path('api/user/register/', RegisterUserView.as_view(), name='api_register_user'),
    path('api/user/register_superuser/', CreateSuperUserAPIView.as_view(), name='api_register_superuser'),

    path('api/media/save/', SaveMedia.as_view(), name='api_save_media'),
    path('api/media/search_by_title/', SearchMediaByTitle.as_view(), name='api_search_media_by_title'),
    path('api/media/all/', ListAllMedia.as_view(), name='api_list_all_media'),
    path('api/media/delete/', DeleteMedia.as_view(), name='api_delete_media'),
    path('api/media/update/', UpdateMedia.as_view(), name='api_update_media'),

    path('api/media/filter/category/', FilterMediaByCategory.as_view(), name='api_filter_media_category'),
    path('api/media/filter/genre/', FilterMediaByGenre.as_view(), name='api_filter_media_genre'),
    path('api/media/filter/release_date/', FilterMediaByReleaseDate.as_view(), name='api_filter_media_release_date'),
    path('api/media/filter/production_studio/', FilterMediaByProductionStudio.as_view(), name='api_filter_media_studio'),
    path('api/media/filter/director/', FilterMediaByDirector.as_view(), name='api_filter_media_director'),

    path('api/media/categories/', ListAllCategories.as_view(), name='api_list_categories'),
    path('api/media/categories/create/', CreateCategory.as_view(), name='api_create_category'),
    path('api/media/categories/delete/', DeleteCategory.as_view(), name='api_delete_category'),
    path('api/media/categories/update/', UpdateCategory.as_view(), name='api_update_category'),

    path('api/media/production/detail/', DetailProductionInfo.as_view(), name='api_production_detail'),
    path('api/media/production/create/', CreateProductionInfo.as_view(), name='api_create_production'),

    path('api/review/create/', CreateReview.as_view(), name='api_create_review'),
    path('api/review/delete/', DeleteReview.as_view(), name='api_delete_review'),
    path('api/review/update/', UpdateReview.as_view(), name='api_update_review'),

    path('api/review/filter/media/', FilterReviewsByMedia.as_view(), name='api_filter_reviews_media'),
    path('api/review/list/user/', ListUserReviews.as_view(), name='api_list_user_reviews'),

    path('api/review/list/latest/', ListLatestReviews.as_view(), name='api_list_latest_reviews'),
    path('api/review/list/top_rated/', ListTopRatedReviews.as_view(), name='api_list_top_rated_reviews'),

    path('api/review/detail/', DetailReview.as_view(), name='api_review_detail'),
    path('api/review/all/', ListAllReviews.as_view(), name='api_list_all_reviews'),
    path('api/review/like/', LikeReview.as_view(), name='api_like_review'),

    path('api/lists/save/', SaveLists.as_view(), name='api_save_lists'),
    path('api/lists/delete/', DeleteLists.as_view(), name='api_delete_lists'),
    path('api/lists/update_category/', UpdateListCategory.as_view(), name='api_update_list_category'),
    path('api/lists/create_category/', CreateListCategory.as_view(), name='api_create_list_category'),
    path('api/lists/delete_category/', DeleteListCategory.as_view(), name='api_delete_list_category'),
    path('api/lists/user_lists/', GetUserLists.as_view(), name='api_get_user_lists'),
    path('api/lists/add_media/', AddMediaToList.as_view(), name='api_add_media_to_list'),
    path('api/lists/remove_media/', RemoveMediaFromList.as_view(), name='api_remove_media_from_list'),
]
