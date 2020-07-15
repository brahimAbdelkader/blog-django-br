from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import pre_save,post_save

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default_post.jpg', upload_to='post_pics')
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-post_date',)
        
        



class Comment(models.Model):

    name = models.CharField(max_length=50, verbose_name='الاسم')
    email = models.EmailField(verbose_name='البريد')
    body = models.TextField(verbose_name='التعليق')
    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return 'علق {} على {}'.format(self.name, self.post)

    class Meta:

        ordering = ('-comment_date',)


# class PostImage(models.Model):
    
#     image = models.ImageField(
#         default='default_post.jpg', upload_to='post_pics')
#     post = models.OneToOneField(Post, on_delete=models.CASCADE)
    
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

#         img = Image.open(self.image.path)
#         if img.width > 300 or img.height > 300:

#             out_size = (300, 300)
#             img.thumbnail(out_size)
#             img.save(self.image.path)

   
# def create_post(sender, **kwarg): 
           
#            if kwarg['created']:
#                Post.objects.create(post=kwarg['instance'])
     
     
        
# post_save.connect(create_post,sender=Post)
