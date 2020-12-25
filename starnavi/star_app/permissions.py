from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


"curl -X POST http://127.0.0.1:8000/api/user/ -u neverd1m:123 -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjA4MjA1MzQwLCJqdGkiOiJjMjk2YmI3MTg2NDE0MDk2OGY3NzcyNzQzNGJjYzdhNCIsInVzZXJfaWQiOjl9.O2Oklms38qU-iM1gD7JGMJ_A5rEzWIERS1SuIa0butE" -d '{"username": "dkfjghsdkfg" , "password": "123"}'"
