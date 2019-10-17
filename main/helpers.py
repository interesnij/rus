from django.http import HttpResponseBadRequest


def ajax_required(f):
    """Не миксин, но хороший декоратор для проверки, чем запрос является AJAX"""
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()

        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap
