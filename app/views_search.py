from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Paragraph
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    method='post',
    operation_description="Search for paragraphs containing a specific word",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'word': openapi.Schema(type=openapi.TYPE_STRING, description='The word to search for'),
        }
    ),
    responses={
        200: openapi.Response('Success', openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'output': openapi.Schema(type=openapi.TYPE_STRING, description='Output message'),
                'paragraphs': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT), description='Matching paragraphs'),
            }
        )),
        400: 'Bad Request',
        405: 'Method Not Allowed',
    }
)
@api_view(['POST'])
def search_word(request):
    # Check if the request method is POST
    if request.method != 'POST':
        return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # Get the search term from request data
    word = request.data.get('word', '').strip()

    # Check if the search word is empty
    if not word:
        return Response({"error": "Please provide a word to search"}, status=status.HTTP_400_BAD_REQUEST)

    # Get all paragraphs containing the search term
    matching_paragraphs = Paragraph.objects.filter(text__icontains=word)[:10]

    if not matching_paragraphs:
        return Response({"output": f"No paragraphs found containing the word '{word}'"}, status=status.HTTP_200_OK)

    # Extract the paragraph IDs and create the output message
    paragraph_ids = [paragraph.id for paragraph in matching_paragraphs]
    output_message = f"Input - '{word}' | Output: {' and '.join([f'Paragraph {id}' for id in paragraph_ids])} are returned"

    return Response({"output": output_message, "paragraphs": matching_paragraphs.values()}, status=status.HTTP_200_OK)
