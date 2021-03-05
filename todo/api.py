from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import eventsSerializer
from rest_framework.decorators import api_view
from .models import events


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = events.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = eventsSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = eventsSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = events.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


'''@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, id):
    # find tutorial by pk (id)
    try:
        tutorial = events.objects.get(pk = id)
    except events.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tutorial_serializer = eventsSerializer(tutorial)
        return JsonResponse(tutorial_serializer.data)

    elif request.method == 'PUT':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = eventsSerializer(tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tutorial.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'DELETE':
        count = events.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)

'''


def tutorial_list_published():
    tutorials = events.objects.filter(published=True)

    if request.method == 'GET':
        tutorials_serializer = eventsSerializer(tutorials, many=True)
    return JsonResponse(tutorials_serializer.data, safe=False)


@api_view(['PUT', 'DELETE'])
def update_tutorials(request, id):
    task = events.objects.get(pk=id)
    serializer = eventsSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


def delete_tutorials(request, id):

    if request.method == 'DELETE':
        tutorial.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'DELETE':
        count = events.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)
