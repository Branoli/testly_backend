from .models import WoodTable
from .serializers import WoodTableSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, permissions


@api_view(['GET'])
def get_all(request):

    permission_classes = (
        permissions.IsAuthenticated,
    )

    snippets = WoodTable.objects.all()
    serializer = WoodTableSerializer(snippets,
                                     many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_element(request):

    permission_classes = (
        permissions.IsAuthenticated,
    )

    serializer = WoodTableSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_subtree(request, pk):

    permission_classes = (
        permissions.IsAuthenticated,
    )

    try:
        subtree = WoodTable.objects.get(id=pk).get_descendants()
    except WoodTable.DoesNotExist:
        return Response(status=404)

    serializer = WoodTableSerializer(subtree, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_search_text(request, text):

    permission_classes = (
        permissions.IsAuthenticated,
    )

    try:
        subtree = WoodTable.objects.get(text__iexact=text).get_ancestors()
    except WoodTable.DoesNotExist:
        return Response(status=404)

    serializer = WoodTableSerializer(subtree, many=True)
    return Response(serializer.data)