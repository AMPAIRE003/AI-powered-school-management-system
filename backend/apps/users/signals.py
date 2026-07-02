"""
Users app signals.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.users.models import User, UserNotificationPreference


@receiver(post_save, sender=User)
def create_user_notification_preferences(sender, instance, created, **kwargs):
    """
    Create default notification preferences when a user is created.
    """
    if created:
        notification_types = [
            'exam_scheduled',
            'exam_result',
            'fee_due',
            'fee_paid',
            'report_generated',
            'announcement',
        ]
        
        for notif_type in notification_types:
            UserNotificationPreference.objects.get_or_create(
                user=instance,
                notification_type=notif_type,
                defaults={'enabled': True}
            )