from rest_framework import viewsets, permissions
from .models import Post, Comment
from django.contrib.auth.models import User
from .serializers import PostSerializer, CommentSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly, IsAdminUser
from rest_framework.throttling import UserRateThrottle

#과제 2: 쓰롤링 뷰 별 적용

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    throttle_classes = [UserRateThrottle] #과제2 : 게시글 올리는 것을 하루 100회 제한

    filterset_fields =['author__username', 'title'] #'author_username은 장고 ORM에서 자동으로 만들어주는 유저이름
                                                    # 추가 ORM 제공 : author__email, author__id, comment__post__title
    ordering_fields =['created_at', 'title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]  #과제 1: 유저뷰셋 조회 보호

    