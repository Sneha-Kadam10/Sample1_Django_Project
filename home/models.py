from django.db import models

class Quiz(models.Model):
    AGE_GROUP_CHOICES = [
        ("5-7", "5–7 years"),
        ("8-10", "8–10 years"),
        ("11-12", "11–12 years"),
    ]

    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    age_group = models.CharField(max_length=10, choices=AGE_GROUP_CHOICES)

    def __str__(self):
        return f"{self.question} ({self.age_group})"
