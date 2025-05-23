from .serializers import UserLoginSerialzer
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSignupSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class BaseAuthView(APIView):
    permission_classes = [AllowAny]

    def success(self, message, data=None, status_code=status.HTTP_200_OK):
        response_data = {"message": message}
        if data:
            response_data.update(data)
        return Response(response_data, status=status_code)
    
    def error(self, errors, status_code=status.HTTP_400_BAD_REQUEST):
        return Response(errors, status=status_code)
    

class SignupView(BaseAuthView):
    def post(self,request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.success("회원가입이 완료되었습니다.", status_code=status.HTTP_201_CREATED)
        return self.error(serializer.errors)

class LoginView(BaseAuthView):
    def post(self, request):
        serializer = UserLoginSerialzer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)

            response = self.success("로그인 성공")
            response["Authorization"] = f"Bearer {str(refresh.access_token)}"
            response.set_cookie(
                key='refresh_token',
                value=str(refresh),
                httponly=True,
                samesite='Lax',
                secure=False
            )
            return response
        return self.error(serializer.errors)