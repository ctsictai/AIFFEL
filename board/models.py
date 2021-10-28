from django.db import models


class Board(models.Model):
    """
    질문 테이블
    """

    title = models.CharField(max_length=200,)
    context = models.TextField(blank=True, null=True)
    user = models.ForeignKey("user.User", models.DO_NOTHING, related_name="board_user")

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    답변 테이블
    """

    context = models.CharField(max_length=500,)
    user = models.ForeignKey("user.User", models.DO_NOTHING, related_name="comment_user")
    board = models.ForeignKey(Board, models.DO_NOTHING, related_name="comment_board")

