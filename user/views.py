from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from . import models, serializers


class UserRegistration(APIView):

    # authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = serializers.UserRegistSerializer(data=request.data)  # 수정필요
        if serializer.is_valid():
            serializer.save()
            return Response({"results": "success"}, status=201)
        return Response(serializer.errors, status=400)


class UserLogin(TokenObtainPairView):
    serializer_class = serializers.CustomTokenObtainPairSerializer
