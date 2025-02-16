from django.shortcuts import render
from django.http import JsonResponse
from .models import Scheme
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required
@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "").lower()

            if "all schemes" in user_message:
                return JsonResponse({"response": get_all_schemes()})

            elif "eligibility" in user_message:
                return JsonResponse({"response": "Provide details as: 'Age: 25, Income: 300000, Category: OBC'"})

            elif "age:" in user_message and "income:" in user_message and "category:" in user_message:
                return JsonResponse({"response": check_eligibility(user_message)})

            else:
                return JsonResponse({"response": "Ask about 'all schemes' or 'eligibility'."})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)


def get_all_schemes():
    schemes = Scheme.objects.all()
    if not schemes:
        return "No government schemes available."
    
    return "\n".join([f"📌 {s.name}: {s.description} 🔗 {s.link}" for s in schemes])


def check_eligibility(user_message):
    try:
        details = {key.strip(): value.strip() for key, value in 
                   (item.split(":") for item in user_message.split(","))}
        
        age = int(details.get("age", 0))
        income = int(details.get("income", 0))
        category = details.get("category", "").lower()

        eligible_schemes = Scheme.objects.filter(
            min_age__lte=age, max_age__gte=age,
            min_income__lte=income, max_income__gte=income,
            category__icontains=category
        )

        if eligible_schemes.exists():
            return "\n".join([f"✅ {s.name}: {s.description} 🔗 {s.link}" for s in eligible_schemes])
        else:
            return "No schemes found based on your details."

    except Exception:
        return "Invalid format. Please enter: 'Age: 25, Income: 300000, Category: OBC'."

def chatbot_page(request):
    return render(request, "chatbot/index.html")

