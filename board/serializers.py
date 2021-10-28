from rest_framework.serializers import ModelSerializer  # noqa

from . import models


class BoardSerializer(ModelSerializer):
    class Meta:
        model = models.Board
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    class Meta:
        model = models.Comment
        fields = "__all__"


class CommentInBoardSerializer(ModelSerializer):
    comment_in_board = CommentSerializer(source="comment_board", many=True)
    
    class Meta:
        model = models.Board
        fields = ["comment_in_board"]
