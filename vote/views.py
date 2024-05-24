from django.utils import timezone
from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from vote.models import Vote
from vote.serializers import VoteSerializer, VoteCreateSerializer


class VoteViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):

    queryset = Vote.objects.select_related("employee", "menu")
    serializer_class = VoteSerializer

    def get_serializer_class(self):

        if self.action == "create":
            return VoteCreateSerializer

        return self.serializer_class


class CurrentDayResultsView(APIView):

    def get(self, request, *args, **kwargs):
        today = timezone.now().date()
        votes = Vote.objects.filter(voted_at=today)

        results = {}

        for vote in votes:

            menu_key = (
                f"Restaurant - {vote.menu.restaurant.name},"
                f" menu id - {vote.menu.id}"
            )

            if menu_key in results:
                results[menu_key] += 1

            else:
                results[menu_key] = 1

        return Response(results, status=status.HTTP_200_OK)
