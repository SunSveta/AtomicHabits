from django.contrib import admin

from habits.models import Habit
from users.models import User


# Register your models here.

@admin.register(Habit)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user', 
        'place', 
        'time', 
        'action', 
        'pleasant_habit', 
        'related_habit',
        'frequency',
        'bonus',
        'time_to_complete',
        'status',
    )


admin.site.register(User)