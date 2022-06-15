from rest_framework import routers

from django.urls import include, path

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register('follow', FollowViewSet, basename='follow')
router.register(r'posts/(?P<post_pk>\d+)/comments',
                CommentViewSet, basename='comments')

VERSION_PARAM = 'v1'

urlpatterns = [
    path(f'{VERSION_PARAM}/', include(router.urls)),
    path(f'{VERSION_PARAM}/', include('djoser.urls.jwt')),
]
