from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Match
from polls.serializers import MatchSerializer
from rest_framework.response import Response


class MatchList(APIView):
    
    def get(self, request):
        match =Match.objects.all()
        requested_team = self.request.query_params.get('home_team', None)
        if requested_team is not None:
            match = match.filter(home_team=requested_team)
            
        serializer = MatchSerializer(match, many = True)
        return Response(serializer.data)
    
    def post(self):
        pass