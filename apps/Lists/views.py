from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ListCategory, List
from apps.MediaList.models import Media
from apps.Users.models import User

class SaveLists(APIView):

    def save_list_name(self, name):

        ListCategory.objects.create(name-name)
        list_name = ListCategory.objects.get(name=name)
        return list_name

    def post(self, request):
        
        for data in request.data:
            list_name = data['list name']
            medias = data['media']
            user = data['user']

            list_name_obj = self.save_list_name(name=list_name)
            user_obj = User.objects.get(username=user)

            for media in medias:
                media_obj = Media.objects.get(title=media)
                if not List.objects.filter(category=list_name_obj,
                                            user=user_obj).exists():
                    
                    List.objects.create(category=list_name_obj,
                                        user=user_obj)
                    
                    list_obj = List.objects.filter(category=list_name_obj,
                                            user=user_obj)
                    
                    list_obj.media.add(media_obj)

                elif List.objects.filter(category=list_name_obj,
                                        user=user_obj).exists():
                    
                    list_obj = List.objects.filter(category=list_name_obj,
                                            user=user_obj)
                    
                    list_obj.media.add(media_obj)

                else:
                    continue

                return Response({"message": "CREATED"}, status=status.HTTP_201_CREATED)
            
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class DeleteLists(APIView):

    def delete(self, request):
        
        for data in request.data:
            list_name = data['list name']
            medias = data['media']
            user = data['user']

            list_name_obj = ListCategory.objects.get(name=list_name)
            user_obj = User.objects.get(username=user)

            for media in medias:
                media_obj = Media.objects.get(title=media)
                
                list_obj = List.objects.filter(category=list_name_obj,
                                        user=user_obj)
                
                list_obj.media.remove(media_obj)

            return Response({"message": "DELETED"}, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

class CreateListCategory(APIView):

    def post(self, request):
        name = request.data.get('name')
        if name:
            ListCategory.objects.create(name=name)
            return Response({"message": "CATEGORY CREATED"}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class DeleteListCategory(APIView):

    def delete(self, request):
        name = request.data.get('name')
        if name:
            try:
                category = ListCategory.objects.get(name=name)
                category.delete()
                return Response({"message": "CATEGORY DELETED"}, status=status.HTTP_200_OK)
            except ListCategory.DoesNotExist:
                return Response({"message": "CATEGORY NOT FOUND"}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class UpdateListCategory(APIView):

    def put(self, request):
        old_name = request.data.get('old_name')
        new_name = request.data.get('new_name')
        if old_name and new_name:
            try:
                category = ListCategory.objects.get(name=old_name)
                category.name = new_name
                category.save()
                return Response({"message": "CATEGORY UPDATED"}, status=status.HTTP_200_OK)
            except ListCategory.DoesNotExist:
                return Response({"message": "CATEGORY NOT FOUND"}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class AddMediaToList(APIView):

    def post(self, request):
        list_name = request.data.get('list_name')
        media_title = request.data.get('media_title')
        username = request.data.get('username')

        if list_name and media_title and username:
            try:
                list_category = ListCategory.objects.get(name=list_name)
                user = User.objects.get(username=username)
                media = Media.objects.get(title=media_title)

                list_obj, created = List.objects.get_or_create(category=list_category, user=user)
                list_obj.media.add(media)

                return Response({"message": "MEDIA ADDED TO LIST"}, status=status.HTTP_200_OK)
            except (ListCategory.DoesNotExist, User.DoesNotExist, Media.DoesNotExist):
                return Response({"message": "LIST, USER, OR MEDIA NOT FOUND"}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class RemoveMediaFromList(APIView):
    def post(self, request):
        list_name = request.data.get('list_name')
        media_title = request.data.get('media_title')
        username = request.data.get('username')

        if list_name and media_title and username:
            try:
                list_category = ListCategory.objects.get(name=list_name)
                user = User.objects.get(username=username)
                media = Media.objects.get(title=media_title)

                list_obj = List.objects.get(category=list_category, user=user)
                list_obj.media.remove(media)

                return Response({"message": "MEDIA REMOVED FROM LIST"}, status=status.HTTP_200_OK)
            except (ListCategory.DoesNotExist, User.DoesNotExist, Media.DoesNotExist, List.DoesNotExist):
                return Response({"message": "LIST, USER, OR MEDIA NOT FOUND"}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class GetUserLists(APIView):

    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            lists = List.objects.filter(user=user)
            response_data = {}

            for lst in lists:
                media_titles = [media.title for media in lst.media.all()]
                response_data[lst.category.name] = media_titles

            return Response(response_data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"message": "USER NOT FOUND"}, status=status.HTTP_404_NOT_FOUND)
                    



