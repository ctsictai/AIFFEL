from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=True)
router.register(r"board", views.BoardViewSet, basename="board")
router.register(r"comment", views.CommentViewSet, basename="comment")


urlpatterns = [
    path("", include(router.urls)),
]
