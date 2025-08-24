# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model

# get_user_model() retrieves your custom user model as set in settings.py
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer to handle new user registration.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # This uses the custom user manager to create a user.
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer to validate user credentials for login.
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError("Must include 'username' and 'password'.")

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Unable to log in with provided credentials.")
        
        # Return the authenticated user instance
        return user

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer to display user profile data.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']