# review/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import CodeSubmission
import openai  # For GPT-based reviews

openai.api_key = ""


def submit_code(request):
    review = None
    if request.method == "POST":
        title = request.POST["title"]
        language = request.POST["language"]
        code = request.POST["code"]
        
        review = generate_code_review(language, code)
        CodeSubmission.objects.create(
            title=title, language=language, code=code, review_result=review
        )
    return render(request, "submit_code.html", {"review": review})


def generate_code_review(language, code):
    prompt = f"Review the following {language} code for issues and suggest improvements:\n\n{code}"
    
    # Using the new API interface
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can also use "gpt-3.5-turbo" for a lighter model
        messages=[{"role": "system", "content": "You are a helpful code review assistant."},
                  {"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]
