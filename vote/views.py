from django.utils import timezone
from rest_framework import status, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from vote.models import Vote
from vote.serializers import VoteSerializer, VoteCreateSerializer


class VoteViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):

    queryset = Vote.objects.select_related("employee", "menu")
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        
        if self.action == "create":
            return VoteCreateSerializer

        return self.serializer_class


# Create your views here.
