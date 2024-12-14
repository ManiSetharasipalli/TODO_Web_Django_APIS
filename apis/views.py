from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import TODO
from .serializers import TodoSerializer

class todoAPI(viewsets.ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TodoSerializer


    @action(detail=False, methods=['delete'], url_path='delete_all')
    def delete_all(self, request):
        """
        Custom action to delete all TODO records.
        """
        deleted_count, _ = TODO.objects.all().delete()

        return Response(
            {"message": f"{deleted_count} records deleted."},
            status=status.HTTP_204_NO_CONTENT
        )