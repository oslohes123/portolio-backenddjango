
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
# Create your tests here.
class TestingView(APIView):
    def get(self, request):
        return Response('Testing success', status=status.HTTP_200_OK)
