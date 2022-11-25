from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Team
from django.forms.models import model_to_dict

# Create your views here.
class TeamView(APIView):
    def post(self, request: Request):
        
        new_team: Team = Team.objects.create(**request.data)

        
        return Response(model_to_dict(new_team), 201)


    def get(self, request: Request):
        
        team_list = []
    
        for team in Team.objects.all():
            team_dict = model_to_dict(team)

            team_list.append(team_dict)

        return Response(team_list)


class TeamDetailView(APIView):
    def get(self, request: Request, team_id):
        try:
            team = Team.objects.get(id = team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

        return Response(model_to_dict(team))
    
    def patch(self, request: Request, team_id):
        try:
            team = Team.objects.get(id = team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

        for key, value in request.data.items():
            setattr(team, key, value)

        team.save()

        return Response(model_to_dict(team))

    
    def delete(self, request: Request, team_id):
        try:
            team = Team.objects.get(id = team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, 404)

        team.delete()

        return Response(status=204)
