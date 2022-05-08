from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import Throttled
from account.api.serializers import UserCreateSerializer

from account.api.throttle import UserLoginRateThrottle


class RegisterUserAPIView(CreateAPIView):

    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    throttle_classes = (UserLoginRateThrottle,)

    def perform_create(self, serializer):
        user = serializer.save()

    def throttled(self, request, wait):
        raise Throttled(detail={
            "message": "recaptcha_required",
        })
