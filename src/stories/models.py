from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.conf import settings

def story_media_path(instance, filename):
    return f"stories/{instance.user.id}/{filename}"

class Story(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='stories',
        on_delete=models.CASCADE
    )
    media = models.FileField(upload_to=story_media_path)
    caption = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.TimeField(auto_now_add=True)
    expires_at = models.TimeField(editable=True)
    is_highlighted = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(hours=24)
        super().save(*args, **kwargs)
        
    def is_expired(self):
        return timezone.now() >= self.expires_at
    
    def __str__(self):
        return f"{self.user.username} - Story {self.id}"
    
class StoryViewed(models.Model):
    
    story = models.ForeignKey(
        Story,
        related_name='views',
        on_delete=models.CASCADE
    )
    
    viewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='viewes_stories',
        on_delete=models.CASCADE
    )
    viewed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'stories_viewd'
        managed = True
        verbose_name = 'story_view'
        verbose_name_plural = 'stories_viewed'
        unique_together = ('story','viewer')
        
    # def numbers_
    