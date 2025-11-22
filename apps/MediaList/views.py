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
        
class ListAllMedia(APIView):

    def get(self, request):

        media = Media.objects.all()
        serializer = MediaSerializer(media, many=True).data

        return Response(serializer, status=status.HTTP_200_OK)
    
class DeleteMedia(APIView):

    def post(self, request):

        for data in request.data:
            title = data['title']

            if Media.objects.filter(title=title).exists():
                Media.objects.filter(title=title).delete()

                return Response({'message': 'DELETED'}, status=status.HTTP_204_NO_CONTENT)
            
            else:
                return Response({'message': 'BAD REQUEST'}, status=status.HTTP_400_BAD_REQUEST)
            
class UpdateMedia(APIView):

    def post(self, request):

        for data in request.data:
            title = data['title']
            new_title = data.get('new_title', None)
            synopsis = data.get('synopsis', None)
            release_date = data.get('release_date', None)
            classification = data.get('classification', None)
            duration = data.get('duration', None)
            genres = data.get('genres', None)
            cover = data.get('cover', None)

            if Media.objects.filter(title=title).exists():
                media_obj = Media.objects.get(title=title)

                if new_title:
                    media_obj.title = new_title
                if synopsis:
                    media_obj.synopsis = synopsis
                if release_date:
                    media_obj.release_date = release_date
                if classification:
                    media_obj.classification = classification
                if duration:
                    media_obj.duration = duration
                if genres:
                    media_obj.genres = genres
                if cover:
                    media_obj.cover = cover

                media_obj.save()

                return Response({'message': 'UPDATED'}, status=status.HTTP_200_OK)
            
            else:
                return Response({'message': 'BAD REQUEST'}, status=status.HTTP_400_BAD_REQUEST)
            
class FilterMediaByCategory(APIView):

    def post(self, request):

        for data in request.data:
            category = data['category']

            if MediaCategory.objects.filter(name__iexact=category).exists():
                category_obj = MediaCategory.objects.get(name__iexact=category)
                media = Media.objects.filter(category=category_obj)
                serializer = MediaSerializer(media, many=True).data

                return Response(serializer, status=status.HTTP_200_OK)
            
            else:
                return Response({'message': 'BAD REQUEST'}, status=status.HTTP_400_BAD_REQUEST)
            
class FilterMediaByGenre(APIView):

    def post(self, request):

        for data in request.data:
            genre = data['genre']

            media = Media.objects.filter(genres__icontains=genre)
            serializer = MediaSerializer(media, many=True).data

            if media.exists():
                return Response(serializer, status=status.HTTP_200_OK)
            
            else:
                return Response({'message': 'BAD REQUEST'}, status=status.HTTP_400_BAD_REQUEST)
            
class FilterMediaByReleaseDate(APIView):

    def post(self, request):

        for data in request.data:
            release_date = data['release_date']

            media = Media.objects.filter(release_date=release_date)
            serializer = MediaSerializer(media, many=True).data

            if media.exists():
                return Response(serializer, status=status.HTTP_200_OK)
            
            else:
                return Response({'message': 'BAD REQUEST'}, status=status.HTTP_400_BAD_REQUEST)
            
class FilterMediaByProductionStudio(APIView):

    def post(self, request):

        for data in request.data:
            studio = data['studio']

            media = Media.objects.filter(production__studio__iexact=studio)
            serializer = MediaSerializer(media, many=True).data

            if media.exists():
                return Response(serializer, status=status.HTTP_200_OK)
            
            else:
                return Response({'message': 'BAD REQUEST'}, status=status.HTTP_400_BAD_REQUEST)
            
class FilterMediaByDirector(APIView):

    def post(self, request):

        for data in request.data:
            director = data['director']

            media = Media.objects.filter(production__director__iexact=director)
            serializer = MediaSerializer(media, many=True).data

            if media.exists():
                return Response(serializer, status=status.HTTP_200_OK)
            
            else:
                return Response({'message': 'BAD REQUEST'}, status=status.HTTP_400_BAD_REQUEST)
            
class ListAllCategories(APIView):

    def get(self, request):

        categories = MediaCategory.objects.all()
        category_list = [category.name for category in categories]

        return Response({'categories': category_list}, status=status.HTTP_200_OK)

class CreateCategory(APIView):

    def post(self, request):

        for data in request.data:
            category_name = data['category_name']

            if not MediaCategory.objects.filter(name__iexact=category_name).exists():
                MediaCategory.objects.create(name=category_name)

                return Response({'message': 'CATEGORY CREATED'}, status=status.HTTP_201_CREATED)
            
            else:
                return Response({'message': 'BAD REQUEST'}, status=status.HTTP_400_BAD_REQUEST)
            
class DeleteCategory(APIView):
    def post(self, request):

        for data in request.data:
            category_name = data['category_name']

            if MediaCategory.objects.filter(name__iexact=category_name).exists():
                MediaCategory.objects.filter(name__iexact=category_name).delete()

                return Response({'message': 'CATEGORY DELETED'}, status=status.HTTP_204_NO_CONTENT)
            
            else:
                return Response({'message': 'BAD REQUEST'}, status=status.HTTP_400_BAD_REQUEST)

class UpdateCategory(APIView):

    def post(self, request):

        for data in request.data:
            category_name = data['category_name']
            new_category_name = data['new_category_name']

            if MediaCategory.objects.filter(name__iexact=category_name).exists():
                category_obj = MediaCategory.objects.get(name__iexact=category_name)
                category_obj.name = new_category_name
                category_obj.save()

                return Response({'message': 'CATEGORY UPDATED'}, status=status.HTTP_200_OK)
            
            else:
                return Response({'message': 'BAD REQUEST'}, status=status.HTTP_400_BAD_REQUEST)
            
class DetailProductionInfo(APIView):

    def post(self, request):

        for data in request.data:
            title = data['title']

            if Media.objects.filter(title__iexact=title).exists():
                media_obj = Media.objects.get(title__iexact=title)
                production_obj = media_obj.production

                production_info = {
                    'actors': production_obj.actor,
                    'director': production_obj.director,
                    'studio': production_obj.studio
                }

                return Response(production_info, status=status.HTTP_200_OK)
            
            else:
                return Response({'message': 'BAD REQUEST'}, status=status.HTTP_400_BAD_REQUEST)

class CreateProductionInfo(APIView):

    def post(self, request):

        for data in request.data:
            actors = data['actors']
            director = data['director']
            studio = data['studio']

            if not MediaProduction.objects.filter(actor=actors, director=director, studio=studio).exists():
                MediaProduction.objects.create(actor=actors, director=director, studio=studio)

                return Response({'message': 'PRODUCTION INFO CREATED'}, status=status.HTTP_201_CREATED)
            
            else:
                return Response({'message': 'BAD REQUEST'}, status=status.HTTP_400_BAD_REQUEST)












