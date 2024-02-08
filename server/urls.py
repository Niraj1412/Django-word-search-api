from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Create schema view for Swagger documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Django Backend Documentation",
        default_version='v1',
        description="API endpoints for user login, paragraph creation, and word search.",
    ),
    public=True,
)
paragraph_payload = {
    "paragraphs": [
        {
            "text": "This is the first paragraph."
        },
        {
            "text": "This is the second paragraph."
        }
    ]
}

search_word_payload = {
    "word": "paragraph"
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),  # Include the URLs from app
    # Swagger documentation URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
