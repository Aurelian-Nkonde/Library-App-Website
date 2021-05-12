
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("website.urls")),
    path("login", auth_view.LoginView.as_view(), name="login"),
    path('logout', auth_view.LogoutView.as_view(), name="logout"),
    path("account/", include("account.urls")),
    path("profile/", include("profiles.urls"))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)