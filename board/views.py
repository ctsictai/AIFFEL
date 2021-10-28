from rest_framework.decorators import action, parser_classes, permission_classes  # noqa
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, mixins, ModelViewSet

from . import models, serializers


class BoardViewSet(ModelViewSet):
    """
    질문 게시판 
    """

    queryset = models.Board.objects.all()
    serializer_class = serializers.BoardSerializer
    filter_backends = []

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = serializers.CommentInBoardSerializer(instance)
        return Response(serializer.data)


class CommentViewSet(GenericViewSet, mixins.CreateModelMixin):
    """
    댓글 저장 
    """

    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

