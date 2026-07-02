"""
Users models for school management system.
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    """
    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('teacher', 'Teacher'),
        ('parent', 'Parent'),
        ('student', 'Student'),
        ('staff', 'Staff'),
    )
    
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='parent',
        help_text='User role in the system'
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text='Contact phone number'
    )
    profile_picture = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True,
        help_text='User profile picture'
    )
    address = models.TextField(
        blank=True,
        null=True,
        help_text='User address'
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text='City'
    )
    state = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text='State/Province'
    )
    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text='Country'
    )
    postal_code = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text='Postal/ZIP code'
    )
    is_active = models.BooleanField(
        default=True,
        help_text='Whether the user account is active'
    )
    email_verified = models.BooleanField(
        default=False,
        help_text='Whether the user email has been verified'
    )
    phone_verified = models.BooleanField(
        default=False,
        help_text='Whether the user phone has been verified'
    )
    
    # Notification preferences
    email_notifications = models.BooleanField(
        default=True,
        help_text='Receive email notifications'
    )
    sms_notifications = models.BooleanField(
        default=False,
        help_text='Receive SMS notifications'
    )
    push_notifications = models.BooleanField(
        default=True,
        help_text='Receive push notifications'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['role']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"

    def get_role_display(self):
        return dict(self.ROLE_CHOICES).get(self.role, self.role)


class UserNotificationPreference(models.Model):
    """
    User notification preferences.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='notification_preference'
    )
    notification_type = models.CharField(
        max_length=50,
        choices=[
            ('exam_scheduled', 'Exam Scheduled'),
            ('exam_result', 'Exam Result'),
            ('fee_due', 'Fee Due'),
            ('fee_paid', 'Fee Paid'),
            ('report_generated', 'Report Generated'),
            ('announcement', 'Announcement'),
        ]
    )
    enabled = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'notification_type')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.notification_type}"


class AuditLog(models.Model):
    """
    Audit log for tracking system activities.
    """
    ACTION_CHOICES = (
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
        ('login', 'Login'),
        ('logout', 'Logout'),
        ('export', 'Export'),
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='audit_logs'
    )
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    model_name = models.CharField(max_length=100)
    object_id = models.CharField(max_length=100)
    object_repr = models.CharField(max_length=200, blank=True)
    changes = models.JSONField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),
            models.Index(fields=['action', '-created_at']),
            models.Index(fields=['model_name', '-created_at']),
        ]

    def __str__(self):
        return f"{self.user} - {self.action} - {self.model_name}"