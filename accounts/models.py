from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE , related_name='posts')
    body = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.slug}'
    
    def like_counts(self):
        return self.pvote.count()

class Follow(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='followers')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='following')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.from_user} follow => {self.to_user}"
    