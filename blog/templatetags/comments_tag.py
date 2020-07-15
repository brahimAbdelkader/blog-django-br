from django import template
from blog.models import Comment

register = template.Library()


@register.inclusion_tag("blog/last_comments.html")
def last_comment():
    context = {
        'l_comments': Comment.objects.all()[0:5]
    }

    return context
