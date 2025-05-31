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
                    



