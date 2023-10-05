from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # # 1
    # image = models.ImageField(blank=True, upload_to="images/")
    # 2
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    # # 3
    # def articles_image_path(instance,filename):
    #     return f'image/{instance.user.username}/{filename}'
    # image = models.ImageField(blank=True, upload_to='articles_image_path')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)