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
            
class UpdateReview(APIView):

    def post(self, request):

        for item in request.data:
            rate = item['rate']
            comment = item['comment']
            media = item['media']
            user = item['user']

            media_obj = Media.objects.get(title__iexact=media)
            user_obj = User.objects.get(username=user)

            if Review.objects.filter(media=media_obj, user=user_obj).exists():
                review = Review.objects.get(media=media_obj, user=user_obj)
                review.rate = rate
                review.comment = comment
                review.save()

                return Response({"Message": "Review updated"}, status=status.HTTP_200_OK)
            
            else:
                return Response({"Message": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
            
class FilterReviewsByMedia(APIView):

    def post(self, request):

        for item in request.data:
            media = item['media']

            media_obj = Media.objects.get(title__iexact=media)

            if Review.objects.filter(media=media_obj).exists():
                reviews = Review.objects.filter(media=media_obj)
                serialized_reviews = [{
                    "user": review.user.username,
                    "rate": review.rate,
                    "comment": review.comment} for review in reviews]

                return Response({"reviews": serialized_reviews}, status=status.HTTP_200_OK)
            
            else:
                return Response({"Message": "No reviews found for this media"}, status=status.HTTP_404_NOT_FOUND)
            
class ListUserReviews(APIView):

    def post(self, request):

        for item in request.data:
            user = item['user']

            user_obj = User.objects.get(username=user)

            if Review.objects.filter(user=user_obj).exists():
                reviews = Review.objects.filter(user=user_obj)
                serialized_reviews = [{
                    "media": review.media.title,
                    "rate": review.rate,
                    "comment": review.comment} for review in reviews]

                return Response({"reviews": serialized_reviews}, status=status.HTTP_200_OK)
            
            else:
                return Response({"Message": "No reviews found for this user"}, status=status.HTTP_404_NOT_FOUND)

class ListLatestReviews(APIView):

    def get(self, request):

        reviews = Review.objects.all().order_by('-id')[:10]
        serialized_reviews = [{
            "media": review.media.title,
            "user": review.user.username,
            "rate": review.rate,
            "comment": review.comment} for review in reviews]

        return Response({"latest_reviews": serialized_reviews}, status=status.HTTP_200_OK)
    
class ListTopRatedReviews(APIView):

    def get(self, request):

        reviews = Review.objects.all().order_by('-rate')[:10]
        serialized_reviews = [{
            "media": review.media.title,
            "user": review.user.username,
            "rate": review.rate,
            "comment": review.comment} for review in reviews]

        return Response({"top_rated_reviews": serialized_reviews}, status=status.HTTP_200_OK)

class DetailReview(APIView):

    def post(self, request):

        for item in request.data:
            media = item['media']
            user = item['user']

            media_obj = Media.objects.get(title__iexact=media)
            user_obj = User.objects.get(username=user)

            if Review.objects.filter(media=media_obj, user=user_obj).exists():
                review = Review.objects.get(media=media_obj, user=user_obj)
                serialized_review = {
                    "media": review.media.title,
                    "user": review.user.username,
                    "rate": review.rate,
                    "comment": review.comment}

                return Response({"review": serialized_review}, status=status.HTTP_200_OK)
            
            else:
                return Response({"Message": "Review not found"}, status=status.HTTP_404_NOT_FOUND)

class ListAllReviews(APIView):

    def get(self, request):

        reviews = Review.objects.all()
        serialized_reviews = [{
            "media": review.media.title,
            "user": review.user.username,
            "rate": review.rate,
            "comment": review.comment} for review in reviews]

        return Response({"all_reviews": serialized_reviews}, status=status.HTTP_200_OK)
    
class LikeReview(APIView):

    def post(self, request):

        for item in request.data:
            media = item['media']
            user = item['user']

            media_obj = Media.objects.get(title__iexact=media)
            user_obj = User.objects.get(username=user)

            if Review.objects.filter(media=media_obj, user=user_obj).exists():
                review = Review.objects.get(media=media_obj, user=user_obj)
                review.likes += 1
                review.save()

                return Response({"Message": "Review liked"}, status=status.HTTP_200_OK)
            
            else:
                return Response({"Message": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
