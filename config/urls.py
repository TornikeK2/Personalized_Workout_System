from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

from django.shortcuts import redirect

schema_view = get_schema_view(
    openapi.Info(
        title="Fitness Tracker",
        default_version="v1",
        description="Fitness Tracker RESTful API for your Personalized Workout Plan",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email='kacharavatornike178@gmail.com'),
        license=openapi.License(name="Apache-2.0 license"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# Define the redirect view
def redirect_to_swagger(request):
    return redirect("schema-swagger-ui")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("account.urls")),
    path("api/v1/fitness/", include("fitness.urls")),
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("", redirect_to_swagger),  # Redirect root URL to Swagger UI
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

