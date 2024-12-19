from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'Is similar to tarditional Django view',
            'Gives you most control over application logic',
            'is mapped manually o URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})
