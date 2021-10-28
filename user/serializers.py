from rest_framework.serializers import ModelSerializer  # noqa
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from . import models


class UserRegistSerializer(ModelSerializer):
    def create(self, validated_data):
        # print("---------------------------", validated_data)
        user = models.User.objects.create(
            identification=validated_data["identification"], username=validated_data.get("username", None),
        )
        user.set_password(validated_data["password"])

        user.save()
        return user

    class Meta:
        model = models.User
        fields = ["identification", "username", "password"]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        # assign token
        data["identification"] = attrs["identification"]
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data
