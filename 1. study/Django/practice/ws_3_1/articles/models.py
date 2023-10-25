from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s/%s에 생성된 %s번글 - %s:%s" % (self.created_at.month, self.created_at.day, self.pk, self.title, self.content)