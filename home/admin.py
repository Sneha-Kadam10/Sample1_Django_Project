from django.contrib import admin
from .models import Quiz

class QuizAdmin(admin.ModelAdmin):
    list_display = ("question", "age_group", "correct_answer")
    list_filter = ("age_group",)

admin.site.register(Quiz, QuizAdmin)
