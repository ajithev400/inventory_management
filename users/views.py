from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class UserView(APIView):
    """
    This class-based view handles all CRUD operations for the User model.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id=None):
        """
        Retrieve a list of all users or a specific user by user_id.
        """
        if user_id:
            user = get_object_or_404(User, id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

    def put(self, request, user_id):
        """
        Update an existing user by user_id.
        """
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        """
        Delete a user by user_id.
        """
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class CreateUserView(APIView):
    """
    This class-based view handles the creation of new users.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Create a new user.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ObtainTokenAPIView(APIView):
    """
    API View to obtain JWT access and refresh tokens.
    POST request with email and password to receive tokens.
    """
    permission_classes = [AllowAny] 
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Both email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        
        user = authenticate(request, username=email, password=password)
        

        if user is None:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.is_active:
            return Response({"error": "User account is inactive"}, status=status.HTTP_403_FORBIDDEN)

        # Generate refresh and access tokens
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            },
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'message': 'User logged in successfully'
        }, status=status.HTTP_200_OK)
    

class RefreshTokenAPIView(APIView):
    """
    API View to refresh the JWT access and refresh tokens.
    POST request with the refresh token to refresh access.
    """
    def post(self, request):
        refresh_token = request.data.get('refresh_token')

        if not refresh_token:
            return Response({"error": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Refresh the access token using the provided refresh token
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'access_token': access_token,
            'refresh_token': str(refresh),  # Returning the same refresh token
            'message': 'Access token refreshed successfully'
        }, status=status.HTTP_200_OK)