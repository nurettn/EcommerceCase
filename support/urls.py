from django.urls import path

from .views import store_info_view, user_info_view

urlpatterns = [
    path("user_info/", user_info_view, name="user_info"),
    path("store_info/<int:user_id>/", store_info_view, name="store_info"),
]
