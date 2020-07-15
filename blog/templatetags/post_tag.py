from django import template
from blog.models import Post

register = template.Library()
@register.inclusion_tag("blog/last_posts.html")
def last_posts():
    context={
        'l_posts':Post.objects.all()[0:5]
    }
    
    return context