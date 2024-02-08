from django.urls import path
from .views import LoginView, ParagraphView
from .views_search import search_word
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Create schema view for Swagger documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="API endpoints for user login, paragraph creation, and word search.",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

# Sample JSON payloads
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
    "word": "example"
}

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('paragraph/', ParagraphView.as_view(), name='paragraph-create'),
    path('search/', search_word, name='search_word'),

    # Swagger documentation URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
