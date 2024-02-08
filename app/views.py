from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Paragraph, Word, ParagraphWord
from .models import CustomUser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class LoginView(APIView):
    def post(self, request):
        # Your login logic here
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        if user.check_password(password):
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)

class ParagraphView(APIView):
    @swagger_auto_schema(
        operation_description="Create paragraphs",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'paragraphs': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'text': openapi.Schema(type=openapi.TYPE_STRING)
                        }
                    )
                )
            }
        ),
        responses={200: 'Paragraphs saved successfully'},
    )
    def post(self, request):
        try:
            paragraphs = request.data.get('paragraphs', [])
            
            # Check if paragraphs is a list
            if not isinstance(paragraphs, list):
                return Response({"error": "Paragraphs should be provided as a list"}, status=status.HTTP_400_BAD_REQUEST)

            # Create a list to store paragraph objects
            paragraph_objects = []

            for paragraph_data in paragraphs:
                # Extract paragraph text from the input
                paragraph_text = paragraph_data.get('text', '')

                # Check if the paragraph text is empty
                if not paragraph_text.strip():
                    continue  # Skip empty paragraphs

                # Check if the paragraph already exists
                existing_paragraph = Paragraph.objects.filter(text=paragraph_text).first()

                if not existing_paragraph:
                    words = [word.lower() for word in paragraph_text.split()]

                    # Create a new Paragraph object
                    paragraph = Paragraph(text=paragraph_text)

                    # Save the paragraph
                    paragraph.save()

                    # Save the words in the database and associate them with the paragraph using ParagraphWord model
                    for word_text in words:
                        word = Word.objects.get_or_create(word=word_text)[0]
                        ParagraphWord.objects.create(paragraph=paragraph, word=word)

                    # Append the Paragraph object to the list
                    paragraph_objects.append(paragraph)

            # Save all the Paragraph objects outside the loop
            if paragraph_objects:
                Paragraph.objects.bulk_create(paragraph_objects)

            return Response({"message": "Paragraphs saved successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
