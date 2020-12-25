from django.utils import timezone
from rest_framework_simplejwt import authentication

from .models import Profile


class UpdateLastActivityMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    # Библиотека simple_jwt не включает по умолчанию аутентификацию запросов,
    # хотя запрос к /token/ принимается за логин.
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(
            request, 'user'), 'The UpdateLastActivityMiddleware requires authentication middleware to be installed.'

        # без этой строки пользователь считаатся неавторизованным,
        # хотя запросы выполняются, т.к. токен предоставлен.
        auth_res = authentication.JWTAuthentication().authenticate(request)

        # (<User: neverd1m>, {'token_type': 'access', 'exp': 1608383324, 'jti': '4bd95a120e7f4f498f45e40cd7829f71', 'user_id': 1})
        # print(auth_res)

        if auth_res:
            request.user = auth_res[0]

        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            profile.last_request = timezone.now()
            profile.save()
