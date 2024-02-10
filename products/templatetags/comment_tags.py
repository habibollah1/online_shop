from django import template

register = template.Library()


@register.filter
def only_active_comments(comments):
    return comments.filter(active=True)


# register.filter('only_active_comments', only_active_comments)
