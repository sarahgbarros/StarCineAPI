from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Review, Media, User

class CreateReview(APIView):

    def post(self, request):

        for item in request.data:
            rate = item['rate']
            comment = item['comment']
            media = item['media']
            user = item['user']

            media_obj = Media.objects.get(title__iexact=media)
            user_obj = User.objects.get(username=user)

            if not Review.objects.filter(rate=rate, comment=comment,
                                        media=media_obj, user=user_obj).exists():
                
                Review.objects.create(rate=rate, comment=comment,
                                        media=media_obj, user=user_obj)
            
                return Response({"Message": "Review created"}, status=status.HTTP_201_CREATED)

            else:

                return Response({"Message": "Review alread exist for this user"}, status=status.HTTP_400_BAD_REQUEST)
            
class DeleteReview(APIView):

    def post(self, request):

        for item in request.data:
            media = item['media']
            user = item['user']

            media_obj = Media.objects.get(title__iexact=media)
            user_obj = User.objects.get(username=user)

            if Review.objects.filter(media=media_obj, user=user_obj).exists():
                Review.objects.filter(media=media_obj, user=user_obj).delete()

                return Response({"Message": "Review deleted"}, status=status.HTTP_204_NO_CONTENT)
        
            else:
                return Response({"Message": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)