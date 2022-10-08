from rest_framework import viewsets, views
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class AllUserView(views.APIView):

    def get(self, request):
        pquery = User.objects.all()
        serializers = UserSerializer(pquery, many=True)
        return Response({"data": serializers.data})


class currentUserView(views.APIView):

    def get(self, request):
        try:
            email = request.user
            pquery = User.objects.get(email=email)
            serializer = UserSerializer(pquery)
            return Response({"data": serializer.data})
        except:
            return Response({"data": "Error"})


class getAnyUser(views.APIView):

    def get(self, request, pk):

        try:
            pquery = User.objects.get(id=pk)
            serializer = UserSerializer(pquery)
            return Response({"data": serializer.data})
        except:
            return Response({"data": "Error"})
