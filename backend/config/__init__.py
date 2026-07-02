"""
Django initialization for school management system.
"""
import os
from config.celery import app as celery_app

__all__ = ('celery_app',)

default_app_config = 'config.apps.Config'