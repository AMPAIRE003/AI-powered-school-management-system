"""
Users app serializers.
"""
from rest_framework import serializers
from apps.users.models import User, UserNotificationPreference


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'role', 'phone_number', 'profile_picture', 'address',
            'city', 'state', 'country', 'postal_code', 'is_active',
            'email_verified', 'phone_verified', 'email_notifications',
            'sms_notifications', 'push_notifications', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'email_verified', 'phone_verified']


class UserDetailSerializer(UserSerializer):
    """
    Detailed serializer for User model with additional information.
    """
    notification_preferences = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ['notification_preferences']

    def get_notification_preferences(self, obj):
        prefs = UserNotificationPreference.objects.filter(user=obj)
        return UserNotificationPreferenceSerializer(prefs, many=True).data


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating new users.
    """
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name',
            'password', 'password_confirm', 'role', 'phone_number'
        ]

    def validate(self, data):
        if data['password'] != data.pop('password_confirm'):
            raise serializers.ValidationError({'password': 'Passwords do not match.'})
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserNotificationPreferenceSerializer(serializers.ModelSerializer):
    """
    Serializer for UserNotificationPreference model.
    """
    class Meta:
        model = UserNotificationPreference
        fields = ['id', 'notification_type', 'enabled', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']