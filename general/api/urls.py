from rest_framework.routers import SimpleRouter
from general.api.views import ChatViewSet, CommentViewSet, MessageViewSet, PostViewSet, ReactionViewSet, UserViewSet


router = SimpleRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'posts', PostViewSet, basename="posts")
router.register(r'comments', CommentViewSet, basename="comments")
router.register(r'reaction', ReactionViewSet, basename="reaction")
router.register(r'chats', ChatViewSet, basename="chats")
router.register(r'messages', MessageViewSet, basename="messages")

urlpatterns = router.urls
