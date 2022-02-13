from django import template
register=template.Library()


@register.filter
def get_attach(post, request_user):
    return post.get_attach(request_user)

@register.filter
def get_edit_attach(post, request_user):
    return post.get_edit_attach(request_user)

@register.filter
def is_user_voted(survey, request_user_id):
    return survey.is_user_voted(request_user_id)
