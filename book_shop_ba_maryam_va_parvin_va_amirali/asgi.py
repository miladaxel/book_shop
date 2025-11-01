"""
ASGI config for book_shop_ba_maryam_va_parvin_va_amirali project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_shop_ba_maryam_va_parvin_va_amirali.settings')

application = get_asgi_application()
