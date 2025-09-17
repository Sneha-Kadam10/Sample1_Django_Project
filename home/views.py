from django.shortcuts import render, get_object_or_404
from .models import Quiz

# Home page
def index(request):
    return render(request, "home/index.html")

# Age 5-7 page
def age_5_7(request):
    quizzes = Quiz.objects.filter(age_group="5-7")
    return render(request, "home/age_5_7.html", {"quizzes": quizzes})

# Age 8-10 page
def age_8_10(request):
    quizzes = Quiz.objects.filter(age_group="8-10")
    return render(request, "home/age_8_10.html", {"quizzes": quizzes})

# Age 11-12 page
def age_11_12(request):
    quizzes = Quiz.objects.filter(age_group="11-12")
    return render(request, "home/age_11_12.html", {"quizzes": quizzes})

# Quiz view
def quiz_view(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    if request.method == "POST":
        user_answer = request.POST.get("answer")
        correct_answer = quiz.correct_answer
        is_correct = (user_answer == correct_answer)

        # keep track of score in session
        score = request.session.get("score", 0)
        if is_correct:
            score += 1
        request.session["score"] = score

        return render(request, "home/quiz_result.html", {
            "quiz": quiz,
            "user_answer": user_answer,
            "correct_answer": correct_answer,
            "is_correct": is_correct,
            "score": score
        })

    return render(request, "home/quiz.html", {"quiz": quiz})
