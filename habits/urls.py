from django.urls import path

from habits.views import *
from habits.apps import HabitsConfig

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('retrieve/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_retrieve'),
    path('list/', HabitListAPIView.as_view(), name='habit_list'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('destroy/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_destroy'),
    path('public_habits/', PublicHabitListAPIView.as_view(), name='public_habits_list'),
]