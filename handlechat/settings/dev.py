from .base import *

DEBUG = True
ALLOWED_HOSTS = []
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "doesntmatter")
