from rest_framework import status
from rest_framework.decorators import action, parser_classes, permission_classes  # noqa
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet, mixins, ModelViewSet

from . import filters, models, serializers


class BoardViewSet(ModelViewSet):
    """
    질문 게시판 
    """

    queryset = models.Board.objects.all()
    serializer_class = serializers.BoardSerializer
    filter_backends = [filters.BoardSearchFilter, filters.BoardReactionFilter]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.pk
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = serializers.CommentInBoardSerializer(instance)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def reaction(self, request, *args, **kwargs):
        instance = models.BoardReaction.objects.filter(board=self.get_object(), user_id=request.user.pk)
        is_activate = request.data["is_activate"]
        if is_activate == "True":
            is_activate = True
        elif is_activate == "False":
            is_activate = False

        if instance:
            instance.first().is_activate = is_activate
            instance.update(is_activate=is_activate)
        else:
            models.BoardReaction.objects.create(
                board=self.get_object(), user_id=request.user.pk, is_activate=is_activate
            )
        return Response({"results": "success"}, status=200)

    @action(detail=False, methods=["get"])
    def monthly_reaction(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        max_cs = 0
        instance = None
        for qs in queryset:
            count = models.BoardReaction.objects.filter(board=qs, is_activate=True).count()
            if max_cs <= count:
                max_cs = count
                instance = qs

        serializer = self.get_serializer(instance)
        return Response({"results": serializer.data}, status=200)


class CommentViewSet(GenericViewSet, mixins.CreateModelMixin):
    """
    댓글 저장 
    """

    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.pk
        return super().create(request, *args, **kwargs)
