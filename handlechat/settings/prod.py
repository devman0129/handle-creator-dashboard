from .base import *

DEBUG = True
STATIC_URL = "/static/"

MEDIA_URL = "/media/"

MEDIA_ROOT = "/mnt/web/media"
STATIC_ROOT = "/mnt/web/static"

ALLOWED_HOSTS = [
    "creator.askhandle.com",
    "3.83.128.46",
    "localhost",
    "ec2-44-203-48-211.compute-1.amazonaws.com",
    "44.203.48.211",
]

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

CSRF_TRUSTED_ORIGINS = ["https://creator.handlechat.com"]
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
