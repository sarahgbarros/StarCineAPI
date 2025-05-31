from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Media, MediaCategory, MediaProduction
from .serializers import MediaSerializer



class SaveMedia(APIView):

    def get_category(self, category):
        try:
            category_obj = MediaCategory.objects.get(name__iexact=category)
            return category_obj
        except:
            return 'Category not in Db'
    
    def save_production_in_db(self, actors, director, studio):
        try:
            production_obj = MediaProduction.objects.get(actor=actors, director=director, studio=studio)
        except:
            MediaProduction.objects.create(actor=actors, director=director, studio=studio)
            production_obj = MediaProduction.objects.get(actor=actors, director=director, studio=studio)
        return production_obj

    def post(self, request):

        for data in request.data:
            actors = data['actors']
            diretor = data['director']
            studio = data['studio']
            title = data['title']
            synopsis = data['synopsis']
            release_date = data['release_date']
            category = data['category']
            classification = data['classification']
            duration = data['duration']
            genres = data['genres']
            cover = data['cover']

            category_obj = self.get_category(category=category)
            production_obj = self.save_production_in_db(actors=actors, director=diretor, studio=studio)

            if not Media.objects.filter(title=title, category=category_obj, release_date=release_date).exists():
                Media.objects.create(  
                    title=title, synopsis=synopsis,
                    release_date=release_date,
                    category=category_obj,
                    classification=classification,
                    duration=duration,
                    genres=genres,
                    cover=cover,
                    production=production_obj)
            else:
                continue

        return Response({'message': 'CREATED'}, status=status.HTTP_201_CREATED)
        
        
class SearchMediaByTitle(APIView):

    def post(self, request):

        for data in request.data:
            title = data['title']

            if Media.objects.filter(title=title).exists():
                media = Media.objects.filter(title__iexact=title)
                serializer = MediaSerializer(media, many=True).data

            all_media = []
            all_media.extend(serializer)

        if all_media:
            return Response(all_media, status=status.HTTP_200_OK)
        
        else:
            return Response({'message': 'ERROR'}, status=status.HTTP_404_NOT_FOUND)
        













