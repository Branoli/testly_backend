from .models import WoodTable
from .serializers import WoodTableSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_all(request):

    snippets = WoodTable.objects.all()
    serializer = WoodTableSerializer(snippets,
                                     many=True)
    return Response(serializer.data)