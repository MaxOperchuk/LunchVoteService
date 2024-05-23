from django.urls import path, include
from rest_framework import routers

from vote.views import VoteViewSet, CurrentDayResultsView


router = routers.DefaultRouter()
router.register("votes", VoteViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path(
        "results/",
        CurrentDayResultsView.as_view(),
        name="current-day-results",
    ),
]

app_name = "vote"
