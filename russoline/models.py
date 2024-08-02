from django.db import models
from users.models import User

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    channel = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.follower} subscribed to {self.channel}'
    
class Content(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    video = models.FileField(upload_to='videos/contents/',null=True,blank=True)
    image = models.ImageField(upload_to='images/contents/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Content {self.text}"
    

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user} liked {self.content.text}'
    

class Comment(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.user} commented to {self.content.text}'


