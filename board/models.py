from django.db import models
from django.db.models.fields.related import create_many_to_many_intermediary_model


class Board(models.Model):
    """
    질문 테이블
    """

    title = models.CharField(max_length=200,)
    context = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    user = models.ForeignKey("user.User", models.DO_NOTHING, related_name="board_user")

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    답변 테이블
    """

    context = models.CharField(max_length=500,)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    user = models.ForeignKey("user.User", models.DO_NOTHING, related_name="comment_user")
    board = models.ForeignKey(Board, models.DO_NOTHING, related_name="comment_board")


class BoardReaction(models.Model):
    """
    질문 좋아요 테이블
    """

    board = models.ForeignKey(Board, models.DO_NOTHING, related_name="board_reaction")
    user = models.ForeignKey("user.User", models.DO_NOTHING, related_name="user_reaction")
    is_activate = models.BooleanField(default=False, help_text="True-reaction false-not reaction")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True, blank=True, null=True)

