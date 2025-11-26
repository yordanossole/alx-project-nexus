from django.db import models
from django.conf import settings


class Feed(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        'posts.Posts',
        on_delete=models.CASCADE,
        related_name='posts_feed'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Feed'
        verbose_name_plural = 'Feeds'

    def __str__(self):
        return f"Feed by {self.user} on {self.post}"

    def __repr__(self):
        return f"Feed({self.id}, {self.user}, {self.post})"
    