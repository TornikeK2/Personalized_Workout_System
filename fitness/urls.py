from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    ExerciseListCreateAPIView,
    ExerciseDetailAPIView,
    WorkoutPlanListCreateAPIView,
    WorkoutPlanDetailAPIView,
    TrackingListAPIView,
    TrackingDetailAPIView,
)

urlpatterns = [
    # Exercise Endpoints
    path(
        "exercises/",
        ExerciseListCreateAPIView.as_view(),
        name="exercise-list-create",
    ),
    path(
        "exercises/<int:pk>/",
        ExerciseDetailAPIView.as_view(),
        name="exercise-detail",
    ),
    # Workout Plan Endpoints
    path(
        "workout-plans/",
        WorkoutPlanListCreateAPIView.as_view(),
        name="workout-plan-list-create",
    ),
    path(
        "workout-plans/<int:pk>/",
        WorkoutPlanDetailAPIView.as_view(),
        name="workout-plan-detail",
    ),
    # Tracking Endpoints
    path("tracking/", TrackingListAPIView.as_view(), name="tracking-list"),
    path(
        "tracking/<int:pk>/",
        TrackingDetailAPIView.as_view(),
        name="tracking-detail",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)