import os

FRONTEND_HOST = os.getenv('FRONTEND_HOST', 'http://localhost')
PORTAL_NAME = os.getenv('PORTAL_NAME', 'MediaCMS')
SECRET_KEY = os.getenv('SECRET_KEY', 'ma!s3^b-cw!f#7s6s0m3*jx77a@riw(7701**(r=ww%w!2+yk2')
REDIS_LOCATION = os.getenv('REDIS_LOCATION', 'redis://redis:6379/1')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv('POSTGRES_NAME', 'mediacms'),
        "HOST": os.getenv('POSTGRES_HOST', 'db'),
        "PORT": os.getenv('POSTGRES_PORT', '5432'),
        "USER": os.getenv('POSTGRES_USER', 'mediacms'),
        "PASSWORD": os.getenv('POSTGRES_PASSWORD', 'mediacms'),
        "OPTIONS": {'pool': True},
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

# CELERY STUFF
BROKER_URL = REDIS_LOCATION
CELERY_RESULT_BACKEND = BROKER_URL

MP4HLS_COMMAND = "/home/mediacms.io/bento4/bin/mp4hls"

DEBUG = os.getenv('DEBUG', 'False') == 'True'

# ============================================================
# LOCKDOWN: single admin user, no public access
# ============================================================

# --- Registration: fully disabled ---
USERS_CAN_SELF_REGISTER = False
REGISTER_ALLOWED = False
USERS_NEEDS_TO_BE_APPROVED = True

# --- Login: require login to access anything ---
LOGIN_ALLOWED = True
GLOBAL_LOGIN_REQUIRED = True

# --- Uploads: only admin (superuser) can upload ---
UPLOAD_MEDIA_ALLOWED = True
CAN_ADD_MEDIA = "advancedUser"

# --- Comments: disabled ---
CAN_COMMENT = "advancedUser"

# --- Interactions: all disabled ---
CAN_LIKE_MEDIA = False
CAN_DISLIKE_MEDIA = False
CAN_REPORT_MEDIA = False
CAN_SHARE_MEDIA = False

# --- Anonymous actions: nothing allowed ---
ALLOW_ANONYMOUS_ACTIONS = []

# --- Members page: admins only ---
CAN_SEE_MEMBERS_PAGE = "admins"
ALLOW_ANONYMOUS_USER_LISTING = False

# --- Media workflow: public within the site (login required anyway) ---
PORTAL_WORKFLOW = "public"
MEDIA_IS_REVIEWED = False

# --- Ratings: disabled ---
ALLOW_RATINGS = False

# --- Video trimmer / replacement: disabled for non-admins ---
ALLOW_VIDEO_TRIMMER = False
ALLOW_MEDIA_REPLACEMENT = False
ALLOW_CUSTOM_MEDIA_URLS = False

# --- Notifications: minimal ---
USERS_NOTIFICATIONS = {
    "MEDIA_ADDED": False,
    "MEDIA_ENCODED": False,
    "MEDIA_REPORTED": False,
}
ADMINS_NOTIFICATIONS = {
    "NEW_USER": True,
    "MEDIA_ADDED": False,
    "MEDIA_ENCODED": False,
    "MEDIA_REPORTED": False,
}
