from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("account.urls")),
    path("", include("chat.urls")),
    path(
        "<path:unknown_path>",
        TemplateView.as_view(template_name="system/404.html"),
        name="404",
    ),
]
