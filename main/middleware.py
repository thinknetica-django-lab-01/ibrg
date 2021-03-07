import re


class MobileMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        is_mobile_re = re.compile(
            r".*(ip(hone|od|ad)|mobile|androidtouch|opera m(ob|in)i|(android|chrome).+mobile)",
            re.IGNORECASE,)

        is_mobile = is_mobile_re.match(request.headers['User-Agent'])

        if is_mobile:
            setattr(request, 'Mobile_Agent', is_mobile)

        return self.get_response(request)
