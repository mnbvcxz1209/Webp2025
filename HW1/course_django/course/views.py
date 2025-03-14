# from django.shortcuts import HttpResponse
# Create your views here.
# def myIndex(request):
#     my_name = request.GET.get('name',"CGU")
#     return HttpResponse("Hello"+my_name)
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class HelloApiView(APIView):
#     def get(self,request):
#         my_name = request.GET.get('name' , None)
#         if my_name:
#             retValue = {}
#             retValue['data'] = 'Hello' + my_name
#             return Response(retValue,status=status.HTTP_200_OK)
#         else:
#             return Response(
#                 {"res":"parameter: name is None"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.core.serializers.json import DjangoJSONEncoder
import json
import logging

from .models import Post

logger = logging.getLogger('django')

@api_view(['GET'])
def add_post(request):
    department = request.GET.get('department','')
    coursetitle = request.GET.get('coursetitle','')
    instructor = request.GET.get('instructor','')
    
    new_post = Post()
    new_post.department = department
    new_post.coursetitle = coursetitle
    new_post.instructor = instructor
    new_post.save()
    logger.debug("******* course_api:" + department)
    if department:
        return Response({"data":department+"insert!"},status=status.HTTP_200_OK)
    else:
        return Response(
            {"res": "parameter: name is None"},
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET'])
def list_post(request):
    posts= Post.objects.all().values()
    return JsonResponse(list(posts),safe=False)
    # return Response({"data":
    #                 json.dumps(
    #                     list(posts),
    #                     sort_keys= True,
    #                     indent=1,
    #                     cls=DjangoJSONEncoder)},
    #                 status=status.HTTP_200_OK)